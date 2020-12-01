import pytest

from year_2020.day_1.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [([1721, 979, 366, 299, 675, 1456], 241861950)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
