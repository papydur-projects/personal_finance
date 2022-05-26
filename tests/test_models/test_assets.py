import pytest
from models.assets import CashAsset, Asset


class TestAsset:

    pass


class TestCashAsset:

    @pytest.fixture
    def cash_asset(self):
        return CashAsset(name='test_account', quantity=1234)

    def test_cash_asset_constructor(self, cash_asset):
        assert cash_asset



