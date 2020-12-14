import pytest

from year_2020.day_14.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 'mem[8] = 11', 'mem[7] = 101', 'mem[8] = 0'], 165)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
