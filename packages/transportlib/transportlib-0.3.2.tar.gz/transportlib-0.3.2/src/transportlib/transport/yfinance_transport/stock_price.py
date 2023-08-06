import datetime
import logging
import traceback
from pathlib import Path
from typing import List, Optional
import yfinance as yf
import pandas as pd
import psycopg2

from transportlib.transport import BaseTransport

from transportlib.utils import dump_dataframe_as_csv, safe_convert_iso_str_to_datetime, get_from_env, get_postgres_conn, get_single_value_from_df


def get_tickers_from_ccass(
        host= None,
        user=None,
        password=None,
        port=None,
        database=None,

):
    logging.info("Fetching tickers from Ccass stock codes")

    conn = get_postgres_conn(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    cur = conn.cursor()

    get_tickers_from_ccass = '''
    SELECT substring(sehk_code,2)||'.hk'  from l0.hkex_ccass_stock hcs where sehk_code < '10000'
    '''
    logging.info('Running SQL')
    logging.info(get_tickers_from_ccass)

    cur.execute(get_tickers_from_ccass)
    result = [tup[0] for tup in cur.fetchall()]

    return result

class HistoricalStockPriceTransport(BaseTransport):

    START_DATETIME = datetime.datetime(year=datetime.datetime.now().year - 1, month=1, day=1)

    def __init__(
            self,
            tickers: Optional[List[str]] = None,
            *args,
            **kwargs,
    ):
        super(HistoricalStockPriceTransport, self).__init__(*args, **kwargs)

        self.start_datetime = self.__class__.START_DATETIME

        # Use HKT
        self.end_datetime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)

        if tickers is None:
            logging.info("No watermark is found. Tickers set to None. Fetching tickers all available HK tickers.")
            tickers = get_tickers_from_ccass()

        logging.info("Going to run for the below tickers.")
        logging.info(tickers)

        self.tickers = tickers

    def run(self):
        for ticker in self.tickers:
            logging.info(f'running ticker {ticker}')

            _start_datetime = self.start_datetime

            if self.watermark_df is not None:
                _start_datetime = get_single_value_from_df(
                    df=self.watermark_df,
                    filter_kv_pairs={
                        'ticker': ticker
                    },
                    tar_col='watermark_col',
                    tar_default_val=self.start_datetime
                )

            logging.info(f'''
            ===================================
            Ticker: {ticker}
            Start Datetime: {_start_datetime}
            End Datetime: {self.end_datetime}
            ====================================
            ''')

            try:
                hist_df: pd.DataFrame = yf.download(
                tickers=ticker,
                start=_start_datetime,
                end=self.end_datetime,
            )
            except KeyboardInterrupt as e:
                # stop and end
                logging.error(traceback.format_exc())
                break
            except Exception as e:
                # Can throw all sorts of errors
                logging.error(traceback.format_exc())
                continue
            else:
                hist_df = hist_df.reset_index()
                hist_df.insert(0, 'ticker', ticker)
                hist_df = hist_df.rename(
                    columns=
                    {
                        'Date': 'date',
                        'Open': 'open',
                        'High': 'high',
                        'Low': 'low',
                        'Close': 'close',
                        'Adj Close': 'adj_close',
                        'Volume': 'volume',
                    }
                )

                # hist_df = pd.concat([hist_df, hist_df])
                dump_dataframe_as_csv(dataframe=hist_df, csv_file_path=self.csv_file_path)

