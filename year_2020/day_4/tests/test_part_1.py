import pytest

from year_2020.day_4.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
