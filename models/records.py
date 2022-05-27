import pandas as pd
from pathlib import Path


class Record:
    def __init__(self, model_type):
        self.dataframe_path = Path(f'src/data/dataframes/{model_type}_df.pkl')
        self.df = self.load_dataframe()

    def create_dataframe(self):
        column_names = ['date', 'total_value', 'assets']

    def load_dataframe(self):
        if self.dataframe_path.is_file():
            return pd.read_pickle(self.dataframe_path)
        else:
            self.create_dataframe()

    def save_dataframe(self):
        self.df.to_pickle(self.dataframe_path)


class CryptoRecord(Record):
    def __init__(self):
        super().__init__(model_type='crypto')


class StockRecord(Record):
    pass


class CashRecord(Record):
    pass
