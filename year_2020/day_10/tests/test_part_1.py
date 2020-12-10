import pytest

from year_2020.day_10.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['28', '33', '18', '42', '31', '14', '46', '20', '48', '47', '24', '23', '49', '45', '19', '38', '39', '11',
       '1', '32', '25', '35', '8', '17', '7', '9', '4', '2', '34', '10', '3'], 220),
     (['16', '10', '15', '5', '1', '11', '7', '19', '6', '12', '4'], 35)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
