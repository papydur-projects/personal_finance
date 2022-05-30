from models.assets import Asset, CashAsset, CryptoAsset
import pytest
from pydantic import ValidationError


class TestAsset:
    def test_asset_constructor(self):
        assert Asset(name='test_asset', quantity=1000)

    @pytest.mark.parametrize('name, quantity',
                             [(123, 1000),
                              (True, 1000),
                              (9.12, 1000)]
                             )
    def test_name_string_only(self, name, quantity):
        with pytest.raises(ValidationError):
            Asset(name=name, quantity=quantity)


class TestCashAsset:
    def test_asset_type(self, cash: CashAsset) -> None:
        assert cash.type == 'cash'

    def test_negative_quantity(self) -> None:
        assert CashAsset(name='debt', quantity=-1000)

    def test_asset_type_immutable(self) -> None:
        asset = CashAsset(name='cash', quantity=1000)
        with pytest.raises(TypeError):
            asset.type = 'other_type'


class TestCryptoAsset:
    def test_asset_type(self, bitcoin: CryptoAsset) -> None:
        assert bitcoin.type == 'crypto'

    def test_asset_type_immutable(self, bitcoin: CryptoAsset) -> None:
        with pytest.raises(TypeError):
            bitcoin.type = 'other_type'
