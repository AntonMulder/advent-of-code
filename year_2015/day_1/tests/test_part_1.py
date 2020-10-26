import pytest

from year_2015.day_1.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [('(())', 0),
     ('()()', 0),
     ('(((', 3),
     ('(()(()(', 3),
     ('))(((((', 3),
     ('())', -1),
     ('))(', -1),
     (')))', -3),
     (')())())', -3),
     ],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
