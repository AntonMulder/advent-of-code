import pytest

from year_2020.day_14.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['mask = 000000000000000000000000000000X1001X', 'mem[42] = 100', 'mask = 00000000000000000000000000000000X0XX',
       'mem[26] = 1'], 208)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
