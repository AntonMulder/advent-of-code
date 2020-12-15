import pytest

from year_2020.day_15.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [([1, 3, 2], 1),
     ([2, 1, 3], 10),
     ([1, 2, 3], 27),
     ([2, 3, 1], 78),
     ([3, 2, 1], 438),
     ([3, 1, 2], 1836)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
