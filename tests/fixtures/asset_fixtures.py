import pytest
from models.assets import Asset, CashAsset, EquityAsset, CryptoAsset


@pytest.fixture
def asset() -> Asset:
    return Asset(name='test_asset', quantity=5000)


@pytest.fixture
def cash() -> CashAsset:
    return CashAsset(name='cash', quantity=1000)


@pytest.fixture
def bitcoin() -> CryptoAsset:
    return CryptoAsset(name='bitcoin', quantity=2, ticker='btc')


@pytest.fixture
def nt_world() -> EquityAsset:
    return EquityAsset(name='nt_world', quantity=5, isin='NL0011225305')