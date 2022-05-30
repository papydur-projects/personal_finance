import abc
from typing import Union

from pydantic import BaseModel, StrictStr, Field


class Asset(BaseModel, abc.ABC):
    name: StrictStr
    quantity: float
    type: str = Field(default='base_asset')

    def add(self, amount: Union[float, int]) -> None:
        self.quantity += amount


class CashAsset(Asset):
    type: str = Field('cash', allow_mutation=False)

    class Config:
        validate_assignment = True


class CryptoAsset(Asset):
    ticker: StrictStr
    type: str = Field('crypto', allow_mutation=False)

    class Config:
        validate_assignment = True


class EquityAsset(Asset):
    isin: StrictStr
    type: str = Field('equity', allow_mutation=False)

    class Config:
        validate_assignment = True


