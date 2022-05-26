from abc import ABC
from pydantic.dataclasses import dataclass
import datetime
from typing import List


@dataclass
class Bucket(ABC):
    assets: List
    date: datetime.date = datetime.date.today()
    total_value = None

    def __post_init__(self):
        self.total_value = self.get_total_value()

    def get_total_value(self):
        total_value = 0
        for asset in self.assets:
            total_value += asset.total_value
        return total_value

    def change_date(self, year, month, day):
        self.date = datetime.date(year, month, day)




