import pytest

from year_2020.day_13.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['939', '7,13,x,x,59,x,31,19'], 295)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
