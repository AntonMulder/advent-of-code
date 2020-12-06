import pytest

from year_2020.day_6.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['abc',
       'a\nb\nc',
       'ab\nac',
       'a\na\na\na',
       'b'], 11)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
