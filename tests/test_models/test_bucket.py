import pytest
from pydantic import ValidationError

from models.assets import CashAsset, CryptoAsset


class TestCashBucket:
    def test_constructor(self, empty_cash_bucket):
        assert empty_cash_bucket

    def test_add_one_asset(self, empty_cash_bucket):
        assets = [CashAsset('cash', 1000)]
        empty_cash_bucket.add_assets(assets)
        assert len(empty_cash_bucket.assets) == 1

    def test_add_asset_list(self, empty_cash_bucket, cash_assets):
        empty_cash_bucket.add_assets(cash_assets)
        assert len(empty_cash_bucket.assets) == 2

    def test_add_asset_validation(self, empty_cash_bucket):
        with pytest.raises(ValueError):
            assets = CashAsset('cash', 1000)
            empty_cash_bucket.add_assets(assets)

    def test_cash_instances_validation(self, empty_cash_bucket):
        with pytest.raises(ValueError):
            assets = [CashAsset('cash', 1000),
                      CryptoAsset('bitcoin', 100, 'btc')]
            empty_cash_bucket.add_assets(assets)



