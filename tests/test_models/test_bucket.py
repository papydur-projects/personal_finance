import pytest
from models.assets import CashAsset
from models.buckets import Bucket
from datetime import date


class TestBucket:

    @pytest.fixture(params=({'date': date.today(),
                             'assets': [CashAsset(name='cash', quantity=1234),
                                        CashAsset(name='debt', quantity=-234)],
                             'expected': 1000},
                            {'date': date(1999, 9, 20),
                             'assets': [CashAsset(name='foo', quantity=23456)],
                             'expected': 23456}
                            ), ids=['2assets', '1asset'])
    def bucket(self, request):
        yield {'bucket': Bucket(date=request.param['date'], assets=request.param['assets']),
               'params': request.param}

    def test_constructor(self, bucket):
        assert bucket['bucket']

    def test_total_value(self, bucket):
        assert bucket['bucket'].total_value == bucket['params']['expected']

