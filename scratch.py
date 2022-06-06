from pycoingecko import CoinGeckoAPI

from models.assets import CashAsset, Asset, CryptoAsset
from models.buckets import Bucket, CashBucket
from models.records import CashRecord


def main():
    asset = CashAsset(name='cash', quantity=1000)
    asset2 = CashAsset(name='debt', quantity=-200)
    bucket = CashBucket()
    bucket.add_asset(asset)
    bucket.add_asset(asset2)

    record = CashRecord()
    record.create_empty_dataframe()
    record.add(bucket)

    print(record.df)


if __name__ == '__main__':
    main()
