import pytest

from year_2015.day_2.part_1 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['2x3x4'], 58),
     (['1x1x10'], 43),
     ],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
