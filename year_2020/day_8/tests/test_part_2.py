import pytest

from year_2020.day_8.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99', 'acc +1', 'jmp -4', 'acc +6'], 8)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
