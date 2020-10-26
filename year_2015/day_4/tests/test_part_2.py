import pytest

from year_2015.day_4.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [('abcdef', 6742839),
     ('pqrstuv', 5714438)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
