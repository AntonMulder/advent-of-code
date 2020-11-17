import pytest

from year_2015.day_14.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
       'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'], 2660)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
