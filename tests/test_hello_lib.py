import pytest
from hshbsh import hello


@pytest.mark.parametrize("name", ['Pete', 'Carlo', 'Tom', 'Johnnie'])
def test_hello(name):
    x = hello(name)
    assert x == 'Hello {}!'.format(name)
