import sys
from nose.tools import ok_

from api import views   

def TestApi():
    def setUp(self):
        print('setUp', file=sys.stderr)

    def tearDown(self):
        print('tearDown', file=sys.stderr)

    def test_foo_bar(self):
        ok_(True)
        ok_(False)
