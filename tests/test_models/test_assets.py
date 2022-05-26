import pytest
from models.assets import CashAsset, Asset
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

    @pytest.mark.parametrize('name, quantity', [
        ('name', 'asd'), (123, 987),
    ])
    def test_asset_constructor_validation(self, name, quantity):
        with pytest.raises(ValidationError):
            DummyAsset(name=name, quantity=quantity)


class TestCashAsset:

    @pytest.fixture(params=({'name': 'pos_cash', 'quantity': 1000},
                            {'name': 'neg_cash', 'quantity': -98},))
    def cash_asset(self, request):
        yield {'asset': CashAsset(name=request.param['name'], quantity=request.param['quantity']),
               'params': request.param}

    def test_cash_asset_constructor(self, cash_asset):
        assert cash_asset['asset']

    def test_get_total_value(self, cash_asset):
        assert cash_asset['asset'].get_total_value() == cash_asset['params']['quantity']



