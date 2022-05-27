import pytest
from models.assets import CashAsset, CryptoAsset


class TestCashBucket:
    def test_constructor(self, empty_cash_bucket):
        assert empty_cash_bucket

    def test_allowed_asset_type(self, empty_cash_bucket):
        assert empty_cash_bucket.allowed_asset_type == CashAsset

    def test_add_one_asset(self, empty_cash_bucket):
        asset = CashAsset('cash', 1000)
        empty_cash_bucket.add_asset(asset)
        assert len(empty_cash_bucket.assets) == 1

    def test_add_two_assets(self, empty_cash_bucket):
        asset = CashAsset('cash', 1000)
        empty_cash_bucket.add_asset(asset)
        asset = CashAsset('debt', -100)
        empty_cash_bucket.add_asset(asset)
        assert len(empty_cash_bucket.assets) == 2

    def test_add_wrong_asset_type(self, empty_cash_bucket):
        with pytest.raises(TypeError) as e:
            asset = CryptoAsset('bitcoin', 1000, 'btc')
            empty_cash_bucket.add_asset(asset)


class TestCryptoBucket:
    pass





