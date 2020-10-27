import pytest

from year_2015.day_5.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['qjhvhtzxzqqjkmpb', 'xxyxx', 'qjhvhtzxzqwjkmpb'], 2),
     (['qjhvhtzxzqqjkmpb', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy'], 1)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
