from abc import ABC, abstractmethod
from pycoingecko import CoinGeckoAPI
from pydantic import BaseModel, Field, ValidationError
import datetime
from typing import List, Set
from collections.abc import Iterable

from models.assets import CashAsset, Asset


class Bucket(ABC, BaseModel):
    assets: List = Field(default_factory=list)
    date: datetime.date = datetime.date.today()
    total_value: float = Field(init=False, default=None)

    def get_total_value(self):
        total_value = 0
        for asset in self.assets:
            total_value += asset.total_value
        return total_value

    @staticmethod
    def validate_assets(assets, asset_type):
        if not isinstance(assets, Iterable):
            raise ValueError('function expects list of assets')
        if not all(isinstance(asset, asset_type) for asset in assets):
            raise ValueError(f'not all assets were of type {asset_type}')

    @abstractmethod
    def add_assets(self, assets: Iterable[Asset]):
        self.assets.extend(assets)

    def change_date(self, year, month, day):
        self.date = datetime.date(year, month, day)


class CashBucket(Bucket):
    def add_assets(self, assets):
        self.validate_assets(assets, CashAsset)
        super().add_assets(assets)


class CryptoBucket(Bucket):
    cgapi: CoinGeckoAPI = Field(init=False, default=None)
    supported_tickers: Set = Field(init=False, default=None)

    class Config:
        arbitrary_types_allowed = True

    def __post_init__(self):
        self.cgapi = CoinGeckoAPI()
        self.supported_tickers = self.get_supported_coin_tickers()

    def get_supported_coin_tickers(self):
        coins_list = self.cgapi.get_coins_list()
        supported_tickers = {item['symbol'] for item in coins_list}
        return supported_tickers
