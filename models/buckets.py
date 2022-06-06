import abc
from typing import List

from pydantic import BaseModel, Field

from models.assets import Asset


class Bucket(BaseModel, abc.ABC):
    assets: List[Asset] = Field(default_factory=list)
    type: str = 'base_asset'

    def __contains__(self, key) -> bool:
        return key in self.assets

    def __getitem__(self, name) -> Asset:
        for asset in self.assets:
            if asset == name:
                return asset
        else:
            raise KeyError(f'[{name}] is not an asset in the bucket')

    def add_asset(self, asset: Asset) -> None:
        self.validate_asset_type(asset)
        if asset in self:
            self[asset.name].add(asset.quantity)
        else:
            self.assets.append(asset)

    def validate_asset_type(self, asset: Asset) -> None:
        if asset.type != self.type:
            raise(TypeError(f'Type of the asset [{asset.type}] does not match bucket type [{self.type}]'))

    @abc.abstractmethod
    def get_total_value(self) -> float:
        raise NotImplementedError


class CashBucket(Bucket):
    type: str = Field('cash', allow_mutation=False)

    class Config:
        validate_assignment = True

    def get_total_value(self):
        total = 0
        for asset in self.assets:
            total += asset.quantity
        return total
