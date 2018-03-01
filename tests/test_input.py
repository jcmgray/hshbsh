import pytest
from hshbsh import load_data, Settings, Journey


@pytest.mark.parametrize("fname", [
    'data/a_example.in',
    'data/b_should_be_easy.in',
    'data/c_no_hurry.in',
    'data/d_metropolis.in',
    'data/e_high_bonus.in'])
def test_simple(fname):
    s, js = load_data(fname)

    assert isinstance(s, Settings)
    assert isinstance(js[0], Journey)
