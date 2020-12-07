import pytest

from year_2020.day_5.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['FFFBBBFRLR', 'FFFBBBFRRL', 'FFFFBFFRLR'], 36)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
