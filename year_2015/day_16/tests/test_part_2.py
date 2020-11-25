import pytest

from year_2015.day_16.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['Sue 1: perfumes: 1, cats: 2, children: 1',
       'Sue 2: perfumes: 1, cats: 9, children: 3',
       'Sue 3: perfumes: 1, cats: 2, children: 3'], '2'),
     (['Sue 1: perfumes: 100, cats: 2, children: 36',
       'Sue 2: perfumes: 4, cats: 20, children: 9',
       'Sue 3: perfumes: 1, cats: 23, goldfish: 4'], '3')],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
