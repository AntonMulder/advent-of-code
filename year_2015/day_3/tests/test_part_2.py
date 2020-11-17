import pytest

from year_2015.day_3.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [('^v', 3),
     ('^>v<', 3),
     ('^v^v^v^v^v', 11)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
