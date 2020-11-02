import pytest

from year_2015.day_6.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['turn on 0,0 through 0,0'], 1),
     (['turn off 0,0 through 999,999'], 0),
     (['toggle 0,0 through 999,999'], 2000000)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
