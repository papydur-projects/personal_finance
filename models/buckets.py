from abc import ABC, abstractmethod
from pycoingecko import CoinGeckoAPI
from pydantic import BaseModel, Field
import datetime
from typing import List, Set, Type, Optional

from models.assets import CashAsset, Asset, CryptoAsset


class Bucket(ABC, BaseModel):
    assets: List = Field(default_factory=list)
    date: datetime.date = datetime.date.today()
    allowed_asset_type: Type[Asset] = Field(init=False)
    total_value: float = Field(init=False, default=None)

    def get_total_value(self):
        total_value = 0
        for asset in self.assets:
            total_value += asset.total_value
        return total_value

    def validate_asset(self, asset):
        if not isinstance(asset, self.allowed_asset_type):
            raise TypeError(f'The added asset is not of type {self.allowed_asset_type}')

    def add_asset(self, asset):
        self.validate_asset(asset)
        self.assets.append(asset)

    def change_date(self, year, month, day):
        self.date = datetime.date(year, month, day)


class CashBucket(Bucket):
    allowed_asset_type: Type[CashAsset] = CashAsset


class CryptoBucket(Bucket):
    allowed_asset_type: Type[CryptoAsset] = CryptoAsset
    cgapi: CoinGeckoAPI = Field(init=False, default=None)
    supported_tickers: Set = Field(init=False, default=None)

    class Config:
        arbitrary_types_allowed = True

    def __post_init__(self) -> None:
        self.cgapi = CoinGeckoAPI()
        self.supported_tickers = self.get_supported_coin_tickers()

    def get_supported_coin_tickers(self) -> Set:
        coins_list = self.cgapi.get_coins_list()
        supported_tickers = {item['symbol'] for item in coins_list}
        return supported_tickers


