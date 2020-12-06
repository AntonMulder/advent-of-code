import pytest

from year_2020.day_3.part_2 import run


@pytest.mark.parametrize(
    'test_input, expected',
    [(['..##.......',
       '#...#...#..',
       '.#....#..#.',
       '..#.#...#.#',
       '.#...##..#.',
       '..#.##.....',
       '.#.#.#....#',
       '.#........#',
       '#.##...#...',
       '#...##....#',
       '.#..#...#.#'], 336)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
