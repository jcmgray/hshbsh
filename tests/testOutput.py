import pytest
from hshbsh import write_journeys
from hshbsh import Taxi

def test_check_output():
    taxi1=Taxi()
    taxi2=Taxi()
    taxi1.jids=[2,4,6]
    taxi2.jids=[1,3,5]
    taxis=[taxi1,taxi2]
    output=write_journeys(taxis,"test",False)
    assert output == "3 2 4 6\n3 1 3 5\n"


def test_exceptions():
    taxi1=Taxi()
    taxi2=Taxi()
    taxi1.jids=[x for x in range(10001)]
    taxi2.jids=[1,3,5]
    taxis=[taxi1,taxi2]
    with pytest.raises(TypeError):
        output=write_journeys(taxis,"test",False)

