from typing import Any

from models.assets import Asset, CashAsset, CryptoAsset, EquityAsset
import pytest
from pydantic import ValidationError


class TestAsset:
    def test_asset_constructor(self):
        assert Asset(name='test_asset', quantity=1000)

    @pytest.mark.parametrize('name, quantity',
                             [(123, 1000),
                              (True, 1000),
                              (9.12, 1000)])
    def test_name_string_only(self, name, quantity):
        with pytest.raises(ValidationError):
            Asset(name=name, quantity=quantity)

    def test_add(self) -> None:
        asset = Asset(name='test', quantity=1000)
        asset.add(500)
        assert asset.quantity == 1500
        asset.add(-300.5)
        assert asset.quantity == 1199.5

    def test_equal_to_asset_if_same_name(self) -> None:
        asset1 = Asset(name='test', quantity=1000)
        asset2 = Asset(name='test', quantity=500)
        assert asset1 == asset2

    def test_equal_to_string(self) -> None:
        asset1 = Asset(name='test', quantity=1000)
        assert asset1 == 'test'

    def test_not_equal_if_different_types(self) -> None:
        asset1 = CryptoAsset(name='test', quantity=1000, ticker='btc')
        asset2 = CashAsset(name='test', quantity=500)
        assert asset1 != asset2


class TestCashAsset:
    def test_asset_type(self, cash: CashAsset) -> None:
        assert cash.type == 'cash'

    def test_negative_quantity(self) -> None:
        assert CashAsset(name='debt', quantity=-1000)

    def test_asset_type_immutable(self) -> None:
        asset = CashAsset(name='cash', quantity=1000)
        with pytest.raises(TypeError):
            asset.type = 'other_type'

    def test_equal_to_string(self) -> None:
        asset1 = CashAsset(name='cash', quantity=1000)
        assert asset1 == 'cash'


class TestCryptoAsset:
    def test_asset_type(self, bitcoin) -> None:
        assert bitcoin.type == 'crypto'

    def test_asset_type_immutable(self, bitcoin: CryptoAsset) -> None:
        with pytest.raises(TypeError):
            bitcoin.type = 'other_type'


class TestEquityAsset:
    def test_asset_type(self, nt_world: EquityAsset) -> None:
        assert nt_world.type == 'equity'

    def test_asset_type_immutable(self, nt_world: EquityAsset) -> None:
        with pytest.raises(TypeError):
            nt_world.type = 'other_type'
