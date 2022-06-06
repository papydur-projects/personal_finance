import datetime

import pandas as pd
from pathlib import Path
from pydantic import BaseModel, Field

from models.buckets import Bucket


class Record(BaseModel):

    type: str = Field(default='base_record')
    df: pd.DataFrame = None

    class Config:
        arbitrary_types_allowed = True

    @property
    def dataframe_path(self) -> Path:
        return Path(f'data/dataframes/{self.type}_df.pkl')

    def create_empty_dataframe(self) -> None:
        column_names = ['date', 'value', 'bucket']
        self.df = pd.DataFrame(columns=column_names)
        self.df.set_index('date', inplace=True)

    def add(self, bucket: Bucket) -> None:
        value = bucket.get_total_value()
        self.df = self.df.append({'date': datetime.date.today(), 'value': value, 'bucket': bucket}, ignore_index=True)

    def load_dataframe(self) -> None:
        if self.dataframe_path.is_file():
            self.df = pd.read_pickle(self.dataframe_path)
        else:
            self.create_empty_dataframe()

    def save_dataframe(self):
        self.df.to_pickle(self.dataframe_path)


class CryptoRecord(Record):
    pass


class StockRecord(Record):
    pass


class CashRecord(Record):
    type: str = 'cash'
