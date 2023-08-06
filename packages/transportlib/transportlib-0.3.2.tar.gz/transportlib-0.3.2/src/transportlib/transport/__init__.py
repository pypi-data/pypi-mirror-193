import abc
import logging

import pandas as pd

class BaseTransport(abc.ABC):

    def __init__(self,
                 csv_file_path,
                 watermark_df: pd.DataFrame,
                 *args,
                 **kwargs
                 ):
        self.csv_file_path = csv_file_path
        self.watermark_df = watermark_df


        logging.info('Watermark df as follows:')
        logging.info(self.watermark_df)

    @abc.abstractmethod
    def run(self):
        pass
