import pytest

from models.assets import CashAsset, CryptoAsset, Asset
from models.buckets import CashBucket, Bucket


class TestBucket:
    def test_bucket_constructor(self, empty_bucket: Bucket) -> None:
        assert empty_bucket

    def test_empty_bucket(self, empty_bucket: Bucket) -> None:
        assert not empty_bucket.assets

    def test_add_asset(self, empty_bucket: Bucket, asset: Asset) -> None:
        empty_bucket.add_asset(asset)
        assert len(empty_bucket.assets) == 1

    def test_add_two_assets_with_same_name(self, empty_bucket: Bucket) -> None:
        asset = Asset(name='cash', quantity=1000)
        empty_bucket.add_asset(asset)
        asset = Asset(name='cash', quantity=500)
        empty_bucket.add_asset(asset)
        assert len(empty_bucket.assets) == 1
        assert empty_bucket['cash'].quantity == 1500

    def test_get_item_by_name(self, empty_bucket: Bucket) -> None:
        asset = Asset(name='cash', quantity=1000)
        empty_bucket.add_asset(asset)
        return_asset = empty_bucket['cash']
        assert asset == return_asset

    def test_raise_error_if_asset_not_in_bucket(self, empty_bucket: Bucket) -> None:
        with pytest.raises(KeyError):
            empty_bucket['cash']

    def test_bucket_contains_asset_with_name(self, empty_bucket: Bucket):
        asset = Asset(name='cash', quantity=1000)
        empty_bucket.add_asset(asset)
        assert 'cash' in empty_bucket.assets
        assert 'cash' in empty_bucket

    def test_bucket_contains_asset_with_asset(self, empty_bucket: Bucket):
        asset = Asset(name='cash', quantity=1000)
        empty_bucket.add_asset(asset)
        assert asset in empty_bucket.assets
        assert asset in empty_bucket


class TestCashBucket:
    def test_bucket_type(self, empty_cash_bucket: CashBucket) -> None:
        assert empty_cash_bucket.type == 'cash'

    def test_type_immutable(self, empty_cash_bucket: CashAsset) -> None:
        with pytest.raises(TypeError):
            empty_cash_bucket.type = 'other_type'

    def test_asset_type_validation(self, empty_cash_bucket: CashBucket, bitcoin: CryptoAsset) -> None:
        with pytest.raises(TypeError):
            empty_cash_bucket.validate_asset_type(bitcoin)







