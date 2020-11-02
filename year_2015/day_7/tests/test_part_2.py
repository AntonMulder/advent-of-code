import pytest

from year_2015.day_7.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> h',
       'NOT y -> a'], -457),
     (['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> a', 'y RSHIFT 2 -> g', 'NOT x -> h',
       'NOT y -> i'], 492)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
