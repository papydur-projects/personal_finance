from models.assets_old import CashAsset
from models.buckets_old import CashBucket, CryptoBucket
import pytest


@pytest.fixture
def cash_assets():
    assets = [CashAsset(name='cash', quantity=1234),
              CashAsset(name='debt', quantity=-234)]
    return assets


@pytest.fixture
def empty_cash_bucket() -> CashBucket:
    return CashBucket()


@pytest.fixture
def empty_crypto_bucket() -> CryptoBucket:
    return CryptoBucket()





