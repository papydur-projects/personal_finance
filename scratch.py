from pycoingecko import CoinGeckoAPI

from models.assets import CashAsset, Asset, CryptoAsset
from models.buckets import Bucket


def main():
    crypto = CryptoAsset(name='btc', quantity=1, ticker='btc')
    c_list = [crypto]


    print(crypto in c_list)



if __name__ == '__main__':
    main()
