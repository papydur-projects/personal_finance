import pytest
from models.assets_old import CashAsset, CryptoAsset


class TestCashBucket:
    def test_constructor(self, empty_cash_bucket):
        assert empty_cash_bucket

    def test_allowed_asset_type(self, empty_cash_bucket):
        assert empty_cash_bucket.allowed_asset_type == CashAsset

    def test_add_one_asset(self, empty_cash_bucket):
        asset = CashAsset('cash', 1000)
        empty_cash_bucket.add_assets(asset)
        assert len(empty_cash_bucket.assets) == 1

    def test_add_two_assets(self, empty_cash_bucket):
        asset = CashAsset('cash', 1000)
        empty_cash_bucket.add_assets(asset)
        asset = CashAsset('debt', -100)
        empty_cash_bucket.add_assets(asset)
        assert len(empty_cash_bucket.assets) == 2

    def test_iterable_of_assets(self, empty_cash_bucket, cash_assets):
        empty_cash_bucket.add_assets(cash_assets)
        assert len(empty_cash_bucket.assets) == 2

    def test_add_wrong_asset_type(self, empty_cash_bucket):
        with pytest.raises(TypeError):
            asset = CryptoAsset('bitcoin', 1000, 'btc')
            empty_cash_bucket.add_assets(asset)

    def test_assets_with_same_name(self, empty_cash_bucket):
        assets = [CashAsset('cash', 1000),
                  CashAsset('cash', 1000)]
        empty_cash_bucket.add_assets(assets)
        assert len(empty_cash_bucket.assets) == 1


class TestCryptoBucket:
    def test_crypto_bucket_constructor(self, empty_crypto_bucket):
        assert empty_crypto_bucket

    def test_ticker_validation(self, empty_crypto_bucket):
        with pytest.raises(ValueError):
            crypto_asset = CryptoAsset('bitcoin', 1000, 'sthththn')
            empty_crypto_bucket.add_assets(crypto_asset)





