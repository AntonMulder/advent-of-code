import pytest

from year_2015.day_11.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [('abcdefgh', 'abcdffbb'),
     ('ghijklmn', 'ghjbbcdd')],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
