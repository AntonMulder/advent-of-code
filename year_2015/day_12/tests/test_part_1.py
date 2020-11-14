import pytest

from year_2015.day_12.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [('[1,2,3]', 6),
     ('{"a":2,"b":4}', 6),
     ('[[[3]]]', 3),
     ('{"a":{"b":4},"c":-1}', 3),
     ('{"a":[-1,1]}', 0),
     ('[]', 0)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
