import pytest
from hshbsh import write_journeys
from hshbsh import Taxi

taxi1=Taxi()
taxi2=Taxi()
taxi1.jids=[2,4,6]
taxi2.jids=[1,3,5]

def test_check_output():
    taxis=[taxi1,taxi2]
    for taxi in taxis:
        print(taxi.jids)
    output=write_journeys(taxis,"test",False)
    print(output)
    assert 1 == 2
