from models.assets import CashAsset
from models.buckets import Bucket, CashBucket
import pytest


class DummyBucket(Bucket):
    def get_total_value(self) -> None:
        super().get_total_value()


@pytest.fixture
def empty_bucket() -> DummyBucket:
    return DummyBucket()


@pytest.fixture
def empty_cash_bucket() -> CashBucket:
    return CashBucket()


def get_cash_bucket(q_cash, q_debt) -> CashBucket:
    bucket = CashBucket()
    asset = CashAsset(name='cash', quantity=q_cash)
    asset2 = CashAsset(name='debt', quantity=-q_debt)
    bucket.add_asset(asset)
    bucket.add_asset(asset2)
    return bucket
