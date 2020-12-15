import pytest

from year_2020.day_9.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [([18, 4, 30, 1001, 7, 39, 11, 42, 12, 31, 1, 44, 22, 5, 10, 48, 14, 40, 36, 2, 37, 9, 24, 28, 35, 8, 43, 3, 13,
       17, 4, 6, 23, 7, 11, 12, 15, 16, 72, 38, 10, 59, 5, 41, 14, 18, 19, 21, 24, 9, 1000, 8, 20, 28, 43], 1000)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
