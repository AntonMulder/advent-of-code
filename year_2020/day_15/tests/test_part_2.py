import pytest

from year_2020.day_15.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [([0, 3, 6], 175594),
     ([1, 3, 2], 2578),
     ([2, 1, 3], 3544142),
     ([1, 2, 3], 261214),
     ([2, 3, 1], 6895259),
     ([3, 2, 1], 18),
     ([3, 1, 2], 362)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
