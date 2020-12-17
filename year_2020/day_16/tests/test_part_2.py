import pytest

from year_2020.day_16.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [("""departure class: 0-1 or 4-19
departure row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9""", 132)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
