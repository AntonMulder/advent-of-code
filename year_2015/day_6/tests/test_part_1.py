import pytest

from year_2015.day_6.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['turn on 0,0 through 999,999'], 1000000),
     (['toggle 0,0 through 999,0'], 1000),
     (['turn on 0,0 through 999,999', 'turn off 499,499 through 500,500'], 999996)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
