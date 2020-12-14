import pytest

from year_2020.day_13.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [('17,x,13,19', 3417),
     ('67,7,59,61', 754018),
     ('67,x,7,59,61', 779210),
     ('67,7,x,59,61', 1261476),
     ('1789,37,47,1889', 1202161486)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
