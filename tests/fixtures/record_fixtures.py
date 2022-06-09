
import datetime
import pytest

from models.assets import CashAsset
from models.buckets import CashBucket
from models.records import Record, CashRecord

from tests.fixtures.bucket_fixtures import get_cash_bucket


@pytest.fixture
def empty_cash_record() -> CashRecord:
    return CashRecord()

@pytest.fixture
def cash_record() -> CashRecord:
    record = CashRecord()
    bucket = get_cash_bucket(q_cash=1000, q_debt=-500)
    record.add(bucket, datetime.date.today()-datetime.timedelta(days=10))
    return record

@pytest.fixture
def big_cash_record(cash_record) -> CashRecord:
    bucket = get_cash_bucket(q_cash=2000, q_debt=-400)
    cash_record.add(bucket, datetime.date.today() - datetime.timedelta(days=8))
    bucket = get_cash_bucket(q_cash=1800, q_debt=-200)
    cash_record.add(bucket, datetime.date.today() - datetime.timedelta(days=6))
    return cash_record






