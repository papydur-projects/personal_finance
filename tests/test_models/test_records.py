import pytest

from models.assets import Asset, CashAsset
from models.buckets import CashBucket
from models.records import Record
import datetime


class TestRecord:
    def test_constructor(self) -> None:
        assert Record()

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


