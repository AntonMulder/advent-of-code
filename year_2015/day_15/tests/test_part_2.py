import pytest

from year_2015.day_15.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
