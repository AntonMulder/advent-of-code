import pytest

from year_2015.day_8.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [([r'""'], 2),
     ([r'"abc"'], 2),
     ([r'"aaa\"aaa"'], 3),
     ([r'"\x27"'], 5),
     ([r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'], 12)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
