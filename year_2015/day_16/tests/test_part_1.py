import pytest

from year_2015.day_16.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['Sue 1: perfumes: 1, cars: 2, children: 1',
       'Sue 2: perfumes: 1, cars: 2, children: 2',
       'Sue 3: perfumes: 1, cars: 2, children: 3'], '3'),
     (['Sue 1: perfumes: 100, cars: 2, children: 36',
       'Sue 2: perfumes: 1, cars: 2, children: 3',
       'Sue 3: perfumes: 20, cars: 2, children: 45'], '2')],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
