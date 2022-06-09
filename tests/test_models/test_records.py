from pathlib import Path

import pytest

from models.assets import CashAsset
from models.buckets import CashBucket
from models.records import Record, CashRecord
from config import ROOT_DIR


class TestRecord:
    def test_constructor(self) -> None:
        assert Record().type == 'base_record'

    def test_add_bucket_to_empty_record(self) -> None:
        record = Record()
        bucket = CashBucket()
        asset = CashAsset(name='cash', quantity=1000)
        asset2 = CashAsset(name='debt', quantity=-200)
        bucket.add_asset(asset)
        bucket.add_asset(asset2)
        record.add(bucket)
        assert len(record) == 1
        assert record.df.iloc[0]['value'] == 800

    def test_add_to_bucket(self, cash_record) -> None:
        bucket = CashBucket()
        asset = CashAsset(name='cash', quantity=1500)
        asset2 = CashAsset(name='debt', quantity=-900)
        bucket.add_asset(asset)
        bucket.add_asset(asset2)
        cash_record.add(bucket)
        assert len(cash_record) == 2

    def test_dataframe_path(self):
        record = Record()
        assert record.dataframe_path == ROOT_DIR / 'data' / 'dataframes' / 'base_record_df.pkl'

    def test_save_dataframe(self, cash_record: CashRecord, tmpdir: Path):
        file_path = tmpdir / 'tmp.pkl'
        cash_record.save_dataframe(path=file_path)
        assert Path(file_path).is_file()

    def test_save_dataframe_in_specified_dir(self, cash_record: CashRecord):
        cash_record.save_dataframe()
        assert cash_record.dataframe_path.is_file()

    def test_load_dataframe(self, cash_record: CashRecord, tmpdir: Path):
        file_path = tmpdir / 'tmp.pkl'
        cash_record.save_dataframe(path=file_path)
        assert cash_record.df.iloc[0]['value'] == 800
        assert len(cash_record) == 1
        cash_record.df = None
        with pytest.raises(AttributeError):
            cash_record.df.iloc[0]['value']
        cash_record.load_dataframe(path=file_path)
        assert cash_record.df.iloc[0]['value'] == 800
        assert len(cash_record) == 1

    def test_get_last_bucket(self, big_cash_record: CashRecord):
        bucket = big_cash_record.get_last_bucket()

        #assert bucket['cash'] == 1800
        #assert bucket['debt'] == -200


class TestCashRecord:

    def test_constructor(self):
        assert CashRecord().type == 'cash'

    def test_dataframe_path(self):
        assert CashRecord().dataframe_path == ROOT_DIR / 'data' / 'dataframes' / 'cash_df.pkl'






