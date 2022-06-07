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

    def __len__(self):
        return len(self.df)

    @property
    def dataframe_path(self) -> Path:
        return Path(f'data/dataframes/{self.type}_df.pkl')

    def add(self, bucket: Bucket, date=datetime.date.today()) -> None:
        column_names = ['date', 'value', 'bucket']
        value = bucket.get_total_value()
        new_row = pd.DataFrame({'date': date, 'value': value, 'bucket': [bucket.assets]},
                               columns=column_names)
        if self.df is not None:
            self.df = pd.concat([self.df, new_row])
        else:
            self.df = new_row

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
