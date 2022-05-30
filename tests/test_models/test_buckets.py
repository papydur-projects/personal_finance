import pytest

from models.assets import Asset, CashAsset, CryptoAsset
from models.buckets import CashBucket, Bucket


class TestBucket:
    def test_bucket_constructor(self, empty_bucket: Bucket) -> None:
        assert empty_bucket

    def test_empty_bucket(self, empty_bucket: Bucket):
        assert not empty_bucket.assets


class TestCashBucket:
    def test_bucket_type(self, empty_cash_bucket: CashBucket) -> None:
        assert empty_cash_bucket.type == 'cash'

    def test_type_immutable(self, empty_cash_bucket: CashAsset) -> None:
        with pytest.raises(TypeError):
            empty_cash_bucket.type = 'other_type'

    def test_asset_type_validation(self, empty_cash_bucket: CashBucket, bitcoin: CryptoAsset) -> None:
        empty_cash_bucket.validate_asset_type(bitcoin)

    def test_add_asset(self, empty_cash_bucket: CashBucket, cash: CashAsset):
        empty_cash_bucket.add_asset(cash)
        assert len(empty_cash_bucket.assets) == 1
        assert cash.name in empty_cash_bucket.assets.keys()





