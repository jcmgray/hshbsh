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
	test_owner, excess = initialise_game.initialise_owner( pizza, 2, 5 )
	expected_owner = np.array([[1,1,2,2],[1,1,2,2],[3,3,4,4],[3,3,4,4]], int)

	assert_allclose( test_owner, expected_owner )

def test_initialise_owner_shit_size():

	pizza = np.array([[0,1,1,1,0],[0,0,1,1,1],[0,0,1,1,1],[0,1,0,1,1],[0,0,1,1,1]], int)
	test_owner, excess = initialise_game.initialise_owner( pizza, 2, 5 )
	expected_owner = np.array([[1,1,2,2,0],[1,1,2,2,0],[3,3,4,4,0],[3,3,4,4,0],[0,0,0,0,0]], int)

	assert_allclose( test_owner, expected_owner )

def test_initialise_owner_wrong():

	pizza = np.array([[0,1,1,1,0],[0,0,1,1,1],[0,0,1,1,1],[0,1,0,1,1],[0,0,1,1,1]], int)
	test_owner, excess = initialise_game.initialise_owner( pizza, 2, 5 )
	expected_owner = np.array([[1,1,2,2,7],[1,1,2,2,0],[3,3,4,4,0],[3,3,4,4,0],[0,0,0,0,0]], int)

	assert not np.allclose( test_owner, expected_owner )

def test_initialise_slice_info_perfect_size():

	pizza = np.array([[0,1,1,1],[0,0,1,1],[0,1,1,1],[0,0,1,1]], int)
	excess, slice_info = initialise_game.initialise_owner( pizza, 2, 5 )
	expected_slice_info = [[1,0,1,0,1],[2,0,1,2,3],[3,2,3,0,1],[4,2,3,2,3]]

	assert_allclose( np.array(slice_info), np.array(expected_slice_info) )

def test_initialise_slice_correct():
	
	pizza = np.array([[0,1,1,1],[0,0,1,1],[0,1,1,1],[0,0,1,1]], int)
	owner = np.array([[1,1,2,2,0],[1,1,2,2,0],[3,3,4,4,0],[3,3,4,4,0],[0,0,0,0,0]], int)
	slice_info = [[1,0,1,0,1],[2,0,1,2,3],[3,2,3,0,1],[4,2,3,2,3]]
	slices = 'what is this'

	expected_dict = initialise_game.initialise_slice(pizza, owner, slice_info, slices)

	print(expected_dict)