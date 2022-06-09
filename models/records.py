import datetime

import pandas as pd
from pathlib import Path
from pydantic import BaseModel, Field

from models.buckets import Bucket
from config import ROOT_DIR


class Record(BaseModel):

    type: str = Field(default='base_record')
    df: pd.DataFrame = None

    class Config:
        arbitrary_types_allowed = True

    def __len__(self):
        return len(self.df)

    @property
    def dataframe_path(self) -> Path:
        return ROOT_DIR / Path(f'data/dataframes/{self.type}_df.pkl')

    def add(self, bucket: Bucket, date=datetime.date.today()) -> None:
        self.validate_bucket_type(bucket)
        column_names = ['date', 'value', 'bucket']
        value = bucket.get_total_value()
        new_row = pd.DataFrame({'date': date, 'value': value, 'bucket': bucket}, columns=column_names)
        if self.df is not None:
            self.df = pd.concat([self.df, new_row])
        else:
            self.df = new_row

    def get_last_bucket(self):
        if self.df is not None:
            return self.df.iloc[-1]['bucket']


    def load_dataframe(self, path=None) -> None:
        path = path if path else self.dataframe_path
        self.df = pd.read_pickle(path)

    def save_dataframe(self, path=None):
        path = path if path else self.dataframe_path
        self.df.to_pickle(path)

    def validate_bucket_type(self, bucket: Bucket) -> None:
        if bucket.type != self.type:
            raise(TypeError(f'Type of the bucket [{bucket.type}] does not match record type [{self.type}]'))



class CryptoRecord(Record):
    type: str = 'crypto'


class StockRecord(Record):
    type: str = 'stock'


class CashRecord(Record):
    type: str = 'cash'
