from abc import ABC, abstractmethod
from pydantic.dataclasses import dataclass
from pydantic import StrictStr
from dataclasses import field
from forex_python.converter import CurrencyRates
from typing import List
from pycoingecko import CoinGeckoAPI


@dataclass
class Asset(ABC):
    name: StrictStr
    quantity: float
    total_value: float = field(init=False)

    def __post_init__(self):
        self.total_value = self.get_total_value()

    @abstractmethod
    def get_total_value(self) -> float:
        raise NotImplementedError

    def get_dollar_value(self) -> float:
        converter = CurrencyRates()
        rate = converter.get_rate('EUR', 'USD')
        return rate * self.total_value


@dataclass
class CryptoAsset(Asset):
    ticker: StrictStr

    def get_total_value(self) -> float:
        return self.quantity


@dataclass
class CashAsset(Asset):

    def get_total_value(self) -> float:
        return self.quantity
