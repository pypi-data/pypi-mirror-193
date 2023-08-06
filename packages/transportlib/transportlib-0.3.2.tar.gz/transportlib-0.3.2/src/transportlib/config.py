import datetime
import importlib
import logging
import traceback
from pathlib import Path

import pandas as pd
import yaml
import json

from transportlib.utils import safe_count_csv_rows, write_run_log, get_postgres_conn, get_single_value_from_df
from  transportlib.transport.postgres_transport import get_df_from_sql


def read_config(path_to_config_file):
    with open(path_to_config_file, 'r') as file:
        tasks = yaml.load(file, Loader=yaml.FullLoader)

    logging.info(f"Display config file content:")
    logging.info(json.dumps(tasks, indent=4, sort_keys=True, default=str))

    return tasks


def get_task_by_name(
        tasks,
        target_name,
):
    available_names = []
    task = None
    for candidate_task in tasks:
        candidate_name = candidate_task.get('name')
        available_names.append(candidate_name)

        if target_name == candidate_name:
            task = candidate_task

    if task is None:
        logging.error(f"Cannot find name {target_name}")
        logging.error("Display available names")
        logging.error(json.dumps(available_names, indent=4))
        task = {}

    return task

def get_job_metadata(
        postgres_conn,
        job_name,
):

    sql_template = """
    select start_url,
           export_file_name,
           staging_table_name,
           fully_qualified_staging_table_name,
           l0_table_name,
           fully_qualified_l0_table_name,
           l0_watermark_sql as watermark_sql
           
    from   ctrl.vw_data_ingestion_job
    where  job_name = %s
    and backend = 'transportlib'
    """

    logging.info('Running SQL')
    logging.info(sql_template)

    dat = get_df_from_sql(
        sql_template=sql_template,
        conn=postgres_conn,
        params=[job_name]
    )

    if len(dat) == 0:
        err_msg = f"No metadata is found for job with name {job_name}!"
        logging.error(err_msg)
        raise ValueError(err_msg)

    return dat

def get_watermark_df(
        postgres_conn,
        watermark_sql):

    if type(watermark_sql) == str:
        dat = get_df_from_sql(
            sql_template=watermark_sql,
            conn=postgres_conn,
            params=[],
        )
    else:
        dat = None

    return dat

def execute_config_task(
        task,
):
    # Start time
    start_time = datetime.datetime.utcnow()
    task_name = task.get('name', '')

    # prepare
    output_folder = Path('output')
    output_folder.mkdir(exist_ok=True, parents=True)

    with get_postgres_conn() as postgres_conn:
        # Use context to close the postgres conn
        job_metadata = get_job_metadata(postgres_conn, job_name=task_name)

    export_file_name = job_metadata['export_file_name'].values[0]
    csv_file_path = output_folder.joinpath(f'{export_file_name}.csv')

    if csv_file_path.exists():
        logging.info(f"deleting old file {csv_file_path}")
        csv_file_path.unlink()

    # Get dynamic watermark
    watermark_sql = job_metadata['watermark_sql'].values[0]
    with get_postgres_conn() as postgres_conn:
        # Use context to close the postgres conn
        watermark_df = get_watermark_df(postgres_conn, watermark_sql=watermark_sql)


    # Get Source Transport
    path_to_source_transport_module = task.get('source_transport', {}).get('path_to_module', '')
    source_transport_name = task.get('source_transport', {}).get('transport_name', '')
    source_transport_kwargs = task.get('source_transport', {}).get('kwargs', {})

    # Dynamic Watermark

    source_transport_kwargs.update(
        {
            'csv_file_path': csv_file_path,
            'watermark_df': watermark_df,
        }
    )

    source_transport_module = importlib.import_module(path_to_source_transport_module)
    source_transport = getattr(source_transport_module, source_transport_name)

    # Get Destination Transport
    path_to_destination_transport_module = 'transportlib.transport.postgres_transport'
    destination_transport_name = 'PostgresTransport'
    staging_table_name = job_metadata['staging_table_name'].values[0]
    l0_table_name = job_metadata['l0_table_name'].values[0]

    destination_transport_kwargs = {
        'staging_table_name': staging_table_name,
        'staging_to_l0_sql': '''CALL l0.sp__stg_to_l0__generic(%s, %s);''',
        'staging_to_l0_args': [
            staging_table_name,
            l0_table_name,
        ]
    }
    destination_transport_kwargs.update(
        {
            'csv_file_path': csv_file_path,
            'watermark_df': watermark_df,
        }
    )
    destination_transport_module = importlib.import_module(path_to_destination_transport_module)
    destination_transport = getattr(destination_transport_module, destination_transport_name)

    if source_transport is None:
        raise ValueError('No Source Transport is specified!!!')

    if destination_transport is None:
        raise ValueError('No Destination Transport is specified!!!')

    # Run Source
    try:
        source_transport(**source_transport_kwargs).run()
        destination_transport(**destination_transport_kwargs).run()
    except Exception as e:
        status = 'error'
        stacktrace = traceback.format_exc()
        logging.error(stacktrace)
    else:
        stacktrace = None
        status = 'success'


    # Write log
    finish_time = datetime.datetime.utcnow()
    num_rows = safe_count_csv_rows(csv_file_path=csv_file_path)
    num_items = num_rows - 1 if num_rows != 0 else 0

    write_run_log(task_name=task_name,
                  start_time=start_time,
                  finish_time=finish_time,
                  num_items=num_items,
                  status=status,
                  stacktrace=stacktrace
                  )

    logging.info('Log written successfully')

