import pytest

from year_2015.day_8.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [([r'""'], 4),
     ([r'"abc"'], 4),
     ([r'"aaa\"aaa"'], 6),
     ([r'"\x27"'], 5),
     ([r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'], 19)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
