import pytest

from year_2015.day_12.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [('[1,2,3]', 6),
     ('[1,{"c":"red","b":2},3]', 4),
     ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
     ('[1,"red",5]', 6)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
