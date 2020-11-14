import pytest

from year_2015.day_10.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [('1', 82350),
     ('11', 107312),
     ('21', 139984),
     ('1211', 182376),
     ('111221', 237746)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
