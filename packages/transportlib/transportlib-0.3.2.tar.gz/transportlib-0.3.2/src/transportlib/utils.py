import datetime
import os
import traceback
import csv

import pandas as pd
import logging
from pathlib import Path, PosixPath, WindowsPath

import psycopg2


def get_from_env(
        curr_val,
        env_key: str,
        default_val,
):
    if curr_val is None:
        return os.getenv(env_key, default_val)
    else:
        return curr_val


def dump_dataframe_as_csv(
        dataframe: pd.DataFrame,
        csv_file_path,
):
    """
    If csv_file_path exists, append to it.
    Otherwise, create a new file.
    """
    logging.info('Display dataframe')
    logging.info(dataframe)

    if csv_file_path.exists():
        # append
        dataframe.to_csv(csv_file_path, mode='a', index=False, header=False)
    else:
        # write
        dataframe.to_csv(csv_file_path, mode='w', index=False, header=True)



def safe_convert_iso_str_to_datetime(val,
                                     default=datetime.datetime.utcnow()):
    try:
        dt = datetime.datetime.fromisoformat(val)
    except Exception as e:
        logging.error(traceback.format_exc())
        dt = default

    return dt


def safe_count_csv_rows(csv_file_path: Path) -> int:
    num_rows = 0

    if type(csv_file_path) == str:
        csv_file_path = Path(csv_file_path)

    if type(csv_file_path) in [PosixPath, WindowsPath] and csv_file_path.exists():
        with open(csv_file_path, 'r') as file:
            file = csv.reader(file)
            num_rows = sum(1 for row in file)
    else:
        pass

    logging.info(f"Num rows in file {csv_file_path} is {num_rows}.")

    return num_rows


def write_run_log(
        task_name,
        num_items,
        start_time,
        finish_time,
        status,
        stacktrace,
        host=None,
        port=None,
        user=None,
        password=None,
        database=None,

):
    conn = get_postgres_conn(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
    )
    cur = conn.cursor()

    write_log_sql = """
    INSERT INTO ctrl.transportlib_job_run_log (task_name,start_time,finish_time,items_retrieved,status,stacktrace) VALUES(%s,%s,%s,%s,%s,%s)
    """

    logging.info('Running SQL')
    logging.info(write_log_sql)

    cur.execute(
        write_log_sql,
        (task_name, start_time, finish_time, num_items, status,stacktrace)
    )
    conn.commit()

def get_postgres_conn(
        # Credntials
        host=None,
        port=None,
        user=None,
        password=None,
        database=None,
):
    host = get_from_env(curr_val=host, env_key='POSTGRES_HOST', default_val=None)
    port = get_from_env(curr_val=port, env_key='POSTGRES_PORT', default_val=None)
    user = get_from_env(curr_val=user, env_key='POSTGRES_USER', default_val=None)
    password = get_from_env(curr_val=password, env_key='POSTGRES_PASSWORD', default_val=None)
    database = get_from_env(curr_val=database, env_key='POSTGRES_DATABASE', default_val=None)

    conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)

    return conn

def get_single_value_from_df(
        df,
        tar_col,
        tar_default_val,
        filter_kv_pairs = None
):
    if type(filter_kv_pairs) != dict:
        logging.warning(f'filter_kv_pairs must be a dict. Yours id {filter_kv_pairs}. Type {type(filter_kv_pairs)}')
        logging.warning('setting filter_kv_pairs to empty dict')
        filter_kv_pairs = {}

    if type(df) == pd.DataFrame:
        mask = pd.Series([True]*len(df.index))
        for ref_col, ref_val in filter_kv_pairs.items():
            mask &= (df[ref_col] == ref_val)

        tar_sr = df[mask][tar_col].values

        if len(tar_sr) !=0:
            tar_val = tar_sr[0]
        else:
            logging.info(f'No {tar_col} found! Using default {tar_default_val}')
            tar_val = tar_default_val
    else:
        logging.warning(f'df must be dataframe. Yours is {type(df)}')
        tar_val = tar_default_val

    return tar_val
