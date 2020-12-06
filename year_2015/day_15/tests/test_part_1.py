import pytest

from year_2015.day_15.part_1 import ingredient_score, run


@pytest.mark.skip(reason='Not solved yet')
@pytest.mark.parametrize(
    'test_input, expected',
    [(['Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
       'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'], 62842880)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    [
        ({'capacity': 3, 'durability': 0, 'flavor': 0, 'texture': -3, 'calories': 2}, 0),
        ({'capacity': 3, 'durability': 0, 'flavor': 0, 'texture': -5, 'calories': 2}, -20),
        ({'capacity': -1, 'durability': 0, 'flavor': 4, 'texture': 0, 'calories': 1}, 30),
    ],
)
def test_ingredient_score(test_input, expected):
    assert ingredient_score(10, **test_input) == expected
