from models.assets import CashAsset
from models.buckets import Bucket
import datetime
import pytest

@pytest.fixture
def cash_assets():
    assets = [CashAsset(name='cash', quantity=1234),
              CashAsset(name='debt', quantity=-234)]
    return assets

@pytest.fixture
def buckets(cash_assets):
    buckets = Bucket(date=datetime.date.today())





