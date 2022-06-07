import datetime

from pycoingecko import CoinGeckoAPI

from models.assets import CashAsset, Asset, CryptoAsset
from models.buckets import Bucket, CashBucket
from models.records import CashRecord


def main():
    print(datetime.date.today() - datetime.timedelta(days=10))



if __name__ == '__main__':
    main()
