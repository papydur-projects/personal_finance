import abc

from pydantic import BaseModel, StrictStr, Field


class Asset(BaseModel, abc.ABC):
    name: StrictStr
    quantity: float
    type: str = Field(default=None)


class CashAsset(Asset):
    type: str = Field('cash', allow_mutation=False)

    class Config:
        validate_assignment = True


class CryptoAsset(Asset):
    ticker: StrictStr
    type: str = Field('crypto', allow_mutation=False)

    class Config:
        validate_assignment = True


