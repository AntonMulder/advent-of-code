import pytest

from year_2015.day_11.part_1 import next_password, run


@pytest.mark.parametrize(
    'test_input, expected',
    [('abcdefgh', 'abcdffaa'),
     ('ghijklmn', 'ghjaabcc')],
)
def test_run(test_input, expected):
    assert run(test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    [('aaaaaaaa', 'aaaaaaab'),
     ('aaaaaaaz', 'aaaaaaba'),
     ('aaaazzzz', 'aaabaaaa'),
     ('ghijklmn', 'ghijklmo')],
)
def test_next_password(test_input, expected):
    assert next_password(test_input) == expected
