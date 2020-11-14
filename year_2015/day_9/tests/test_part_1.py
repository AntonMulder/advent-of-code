import pytest

from year_2015.day_9.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['London to Dublin = 464', 'London to Belfast = 518', 'Dublin to Belfast = 141'], 605),
     (['London to Dublin = 464', 'London to Belfast = 120', 'Dublin to Belfast = 141'], 261)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
