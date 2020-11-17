import pytest

from year_2015.day_13.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['Alice would gain 54 happiness units by sitting next to Bob.',
       'Alice would lose 79 happiness units by sitting next to Carol.',
       'Alice would lose 2 happiness units by sitting next to David.',
       'Alice would gain 0 happiness units by sitting next to Anton.',
       'Bob would gain 83 happiness units by sitting next to Alice.',
       'Bob would lose 7 happiness units by sitting next to Carol.',
       'Bob would lose 63 happiness units by sitting next to David.',
       'Bob would gain 0 happiness units by sitting next to Anton.',
       'Carol would lose 62 happiness units by sitting next to Alice.',
       'Carol would gain 60 happiness units by sitting next to Bob.',
       'Carol would gain 55 happiness units by sitting next to David.',
       'Carol would gain 0 happiness units by sitting next to Anton.',
       'David would gain 46 happiness units by sitting next to Alice.',
       'David would lose 7 happiness units by sitting next to Bob.',
       'David would gain 41 happiness units by sitting next to Carol.',
       'David would gain 0 happiness units by sitting next to Anton.',
       'Anton would gain 0 happiness units by sitting next to Alice.',
       'Anton would gain 0 happiness units by sitting next to Bob.',
       'Anton would gain 0 happiness units by sitting next to Carol.',
       'Anton would gain 0 happiness units by sitting next to David.'], 286)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
