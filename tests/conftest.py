import pytest

from models.assets import CashAsset, CryptoAsset
from models.buckets import Bucket, CashBucket


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
def cash() -> CashAsset:
    return CashAsset(name='cash', quantity=1000)


@pytest.fixture
def bitcoin() -> CryptoAsset:
    return CryptoAsset(name='bitcoin', quantity=2, ticker='btc')