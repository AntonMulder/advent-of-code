import pytest

from year_2015.day_17.part_2 import run


@pytest.mark.parametrize(
    'containers, eggnog, expected',
    [([20, 15, 10, 5, 5], 25, 3)],
)
def test_run(containers, eggnog, expected):
    assert run(containers, eggnog) == expected
