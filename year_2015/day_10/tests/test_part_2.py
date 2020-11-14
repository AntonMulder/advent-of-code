import pytest

from year_2015.day_10.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [('1', 1166642),
     ('11', 1520986),
     ('21', 1982710),
     ('1211', 2584304),
     ('111221', 3369156)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
