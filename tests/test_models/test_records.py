import pytest

from models.assets import Asset, CashAsset
from models.records import Record
import datetime


class TestRecord:
    def test_constructor(self) -> None:
        assert Record()

    def test_create_dataframe(self) -> None:
        record = Record()
        record.create_empty_dataframe()
        print(record.df.columns)
        for col_name in ['date', 'total_value', 'bucket']:
            assert col_name in record.df.columns
        assert len(record.df) == 0

    def test_add_bucket(self, empty_record, empty_cash_bucket) -> None:
        asset = CashAsset(name='cash', quantity=1000)
        asset2 = CashAsset(name='debt', quantity=-200)
        empty_cash_bucket.add_asset(asset)
        empty_cash_bucket.add_asset(asset2)
        empty_record.add(empty_cash_bucket)
        assert len(empty_record.df) == 1
        assert empty_record.df.iloc[0]['value'] == 800


