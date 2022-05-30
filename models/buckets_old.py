from abc import ABC, abstractmethod
from typing import Set, Type, Iterable, Union, Dict

from pycoingecko import CoinGeckoAPI
from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass

from models.assets_old import CashAsset, Asset, CryptoAsset


class Bucket(ABC):
    assets: Dict = Field(default_factory=dict)
    allowed_asset_type: Type[Asset] = Field(init=False)
    total_value: float = Field(init=False, default=None)

    def get_total_value(self) -> float:
        total_value = 0
        for asset in self.assets:
            total_value += asset.total_value
        return total_value

    @abstractmethod
    def validate_asset(self, asset: Asset) -> None:
        pass

    def validate_asset_type(self, asset: Asset) -> None:
        if not isinstance(asset, self.allowed_asset_type):
            raise TypeError(f'The added asset is not of type {self.allowed_asset_type}')

    def add_assets(self, assets: Union[Iterable[Asset], Asset]) -> None:
        assets = assets if isinstance(assets, Iterable) else [assets]

        bucket_assets_copy = self.assets.copy()
        for asset in assets:
            self.validate_asset(asset)
            bucket_assets_copy[asset.name] = asset
        self.assets = bucket_assets_copy  # store as class attribute only if all item types were correct


class CashBucket(Bucket):
    allowed_asset_type: Type[CashAsset] = CashAsset

    def validate_asset(self, asset: Asset) -> None:
        self.validate_asset_type(asset)


class CryptoBucket(Bucket):
    allowed_asset_type: Type[CryptoAsset] = CryptoAsset
    cgapi: CoinGeckoAPI = Field(default=None)
    supported_tickers: Set = Field(default=None)

    class Config:
        arbitrary_types_allowed = True

    def __post_init__(self) -> None:
        self.cgapi = CoinGeckoAPI()
        self.supported_tickers = self.get_supported_coin_tickers()

    def get_supported_coin_tickers(self) -> Set:
        coins_list = self.cgapi.get_coins_list()
        supported_tickers = {item['symbol'] for item in coins_list}
        return supported_tickers

    def validate_ticker_id(self, asset: CryptoAsset) -> None:
        if asset.ticker not in self.supported_tickers:
            raise ValueError('The ticker "{asset.ticker}" is not supported')

    def validate_asset(self, asset: CryptoAsset) -> None:
        self.validate_asset_type(asset)
        self.validate_ticker_id(asset)






