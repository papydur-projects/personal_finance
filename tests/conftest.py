import pytest

from models.assets import CashAsset, CryptoAsset, EquityAsset, Asset
from models.buckets import Bucket, CashBucket
from models.records import Record


class DummyBucket(Bucket):
    def get_total_value(self) -> None:
        return None


@pytest.fixture
def empty_bucket() -> DummyBucket:
    return DummyBucket()


@pytest.fixture
def empty_cash_bucket() -> CashBucket:
    return CashBucket()


@pytest.fixture
def asset() -> Asset:
    return Asset(name='test_asset', quantity=5000)


@pytest.fixture
def cash() -> CashAsset:
    return CashAsset(name='cash', quantity=1000)


@pytest.fixture
def bitcoin() -> CryptoAsset:
    return CryptoAsset(name='bitcoin', quantity=2, ticker='btc')


@pytest.fixture
def nt_world() -> EquityAsset:
    return EquityAsset(name='nt_world', quantity=5, isin='NL0011225305')


@pytest.fixture
def empty_record() -> Record:
    record = Record()
    record.create_empty_dataframe()
    return record
