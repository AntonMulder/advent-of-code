import pytest

from year_2020.day_9.part_2 import run


@pytest.mark.parametrize(
    'numbers, invalid_number, expected',
    [(['35', '20', '15', '25', '47', '40', '62', '55', '65', '95', '102',
       '117', '150', '182', '127', '219', '299', '277', '309', '576'], 127, 62)],
)
def test_run(numbers, invalid_number, expected):
    assert run(numbers, invalid_number) == expected
