import pytest

from year_2020.day_2.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc'], 1)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
