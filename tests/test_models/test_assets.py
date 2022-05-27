import pytest
from models.assets import CashAsset, Asset, CryptoAsset
from pydantic.dataclasses import dataclass
from pydantic import ValidationError


@dataclass
class DummyAsset(Asset):
    def get_total_value(self):
        return self.quantity


class TestAsset:

    @pytest.mark.parametrize('name, quantity', [
        ('dummy_asset', 1234),
        ('091_02%', -230),
        ('name', float(1234)),
        ('name2', '1234')
    ])
    def test_asset_constructor_success(self, name, quantity):
        assert DummyAsset(name=name, quantity=quantity)

    def test_name_type_validation(self):
        with pytest.raises(ValidationError):
            DummyAsset(135, 987)

    def test_quantity_type_validation(self):
        with pytest.raises(ValidationError):
            DummyAsset('name', 'a_number')


class TestCashAsset:

    def test_cash_asset_constructor(self):
        assert CashAsset(name='name', quantity=1000)

    def test_get_total_value(self):
        assert CashAsset('pos_cash', 1000).get_total_value() == 1000
        assert CashAsset('neg_cash', -89).get_total_value() == -89


class TestCryptoAsset:

    def test_crypto_asset_constructor(self):
        assert CryptoAsset('bitcoin', 1000, 'btc')



