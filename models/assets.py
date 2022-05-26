from abc import ABC, abstractmethod
from pydantic.dataclasses import dataclass
from pydantic import StrictStr
from dataclasses import field
from forex_python.converter import CurrencyRates


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

    def get_dollar_value(self):
        converter = CurrencyRates()
        rate = converter.get_rate('EUR', 'USD')
        return rate * self.total_value


@dataclass
class CryptoAsset(Asset):
    def get_total_value(self) -> float:
        pass


@dataclass
class CashAsset(Asset):
    def get_total_value(self) -> float:
        return self.quantity


if __name__ == '__main__':
    cash = CashAsset(name=87, quantity=1230.12)
    print(cash)
    print(cash.total_value)
    print(cash.return_dollar_value())
