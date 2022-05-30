import abc
from typing import Dict, Any

from pydantic import BaseModel, Field

from models.assets import Asset


class Bucket(BaseModel, abc.ABC):
    assets: Dict = Field(default_factory=dict)

    def add_asset(self, asset: Asset):
        self.validate_asset_type(asset)
        self.assets[asset.name] = asset

    def validate_asset_type(self, asset: Asset) -> None:
        if asset.type != self.type:
            raise(TypeError(f'Type of the asset [{asset.type}] does not match bucket type [{self.type}]'))

    @abc.abstractmethod
    def get_total_value(self):
        raise NotImplementedError


class CashBucket(Bucket):
    type: str = Field('cash', allow_mutation=False)

    class Config:
        validate_assignment = True

    def get_total_value(self):
        pass
