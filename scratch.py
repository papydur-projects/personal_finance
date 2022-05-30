from pycoingecko import CoinGeckoAPI

from models.assets_old import CashAsset
from models.buckets_old import Bucket


def main():
    class DummyBucket(Bucket):
        def add_assets(self, assets):
            self._add_assets(assets)

    DummyBucket().add_assets(CashAsset(name='cash', quantity=1234))


if __name__ == '__main__':
    main()
