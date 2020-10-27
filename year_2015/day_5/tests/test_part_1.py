import pytest

from year_2015.day_5.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['ugknbfddgicrmopn', 'aaa', 'ugknbfedgicrmopn'], 2),
     (['jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb', 'ugknbfddgicrmopn'], 1)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
