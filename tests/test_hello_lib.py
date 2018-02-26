import pytest
import numpy as np
from numpy.testing import assert_allclose
from hshbsh import hello, initialise_game


@pytest.mark.parametrize("name", ['Pete', 'Carlo', 'Tom', 'Johnnie'])
def test_hello(name):
    x = hello(name)
    assert x == 'Hello {}!'.format(name)

def test_initialise_owner_perfect_size():

	pizza = np.array([[0,1,1,1],[0,0,1,1],[0,1,1,1],[0,0,1,1]], int)
	test_owner = initialise_game.initialise_owner( pizza, 2, 5 )
	expected_owner = np.array([[1,1,2,2],[1,1,2,2],[3,3,4,4],[3,3,4,4]], int)

	assert_allclose( test_owner, expected_owner )

def test_initialise_owner_shit_size():

	pizza = np.array([[0,1,1,1,0],[0,0,1,1,1],[0,0,1,1,1],[0,1,0,1,1],[0,0,1,1,1]], int)
	test_owner = initialise_game.initialise_owner( pizza, 2, 5 )
	expected_owner = np.array([[1,1,2,2,0],[1,1,2,2,0],[3,3,4,4,0],[3,3,4,4,0],[0,0,0,0,0]], int)

	assert_allclose( test_owner, expected_owner )

def test_initialise_owner_wrong():

	pizza = np.array([[0,1,1,1,0],[0,0,1,1,1],[0,0,1,1,1],[0,1,0,1,1],[0,0,1,1,1]], int)
	test_owner = initialise_game.initialise_owner( pizza, 2, 5 )
	expected_owner = np.array([[1,1,2,2,7],[1,1,2,2,0],[3,3,4,4,0],[3,3,4,4,0],[0,0,0,0,0]], int)

	assert not np.allclose( test_owner, expected_owner )
