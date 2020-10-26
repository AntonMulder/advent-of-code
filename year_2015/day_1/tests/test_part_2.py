import pytest

from year_2015.day_1.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(')', 1),
     ('()())', 5)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
