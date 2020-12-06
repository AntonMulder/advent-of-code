import pytest

from year_2020.day_3.part_1 import run


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
       '.#..#...#.#'], 7)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
