import pytest

from year_2015.day_2.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['2x3x4'], 34),
     (['1x1x10'], 14),
     ],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
