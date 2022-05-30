import pytest

from models.assets import CashAsset, CryptoAsset, Asset
from models.buckets import CashBucket, Bucket


class TestBucket:
    def test_bucket_constructor(self, empty_bucket: Bucket) -> None:
        assert empty_bucket

    def test_empty_bucket(self, empty_bucket: Bucket):
        assert not empty_bucket.assets

    def test_add_asset(self, empty_bucket: Bucket, asset: Asset):
        empty_bucket.add_asset(asset)
        assert len(empty_bucket.assets) == 1
        assert asset.name in empty_bucket.assets.keys()


class TestCashBucket:
    def test_bucket_type(self, empty_cash_bucket: CashBucket) -> None:
        assert empty_cash_bucket.type == 'cash'

    def test_type_immutable(self, empty_cash_bucket: CashAsset) -> None:
        with pytest.raises(TypeError):
            empty_cash_bucket.type = 'other_type'

    def test_asset_type_validation(self, empty_cash_bucket: CashBucket, bitcoin: CryptoAsset) -> None:
        with pytest.raises(TypeError):
            empty_cash_bucket.validate_asset_type(bitcoin)







