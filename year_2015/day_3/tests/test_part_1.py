import pytest

from year_2015.day_3.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [('>', 2),
     ('^>v<', 4),
     ('^v^v^v^v^v', 2)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
