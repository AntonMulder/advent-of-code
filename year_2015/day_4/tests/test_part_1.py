import pytest

from year_2015.day_4.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [('abcdef', 609043),
     ('pqrstuv', 1048970)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
