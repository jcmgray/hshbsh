from hshbsh import hello


def test_hello():
    x = hello('Johnnie')
    assert x == 'Hello Johnnie!'
