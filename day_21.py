"""Day 21: RPG Simulator 20XX"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools
from functools import cache

ARMOR = ((13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5))
RINGS = (
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
)
WEAPONS = ((8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0))


def main():
    """Solve day 21 puzzles."""
    with open("data/day_21.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    boss = load_boss(puzzle_input)
    combinations = get_combinations()

    combinations.sort(key=lambda items: sum(item[0] for item in items))

    for combination in combinations:
        if play(combination, boss):
            return sum(item[0] for item in combination)

    return 0


def star_2(puzzle_input):
    """Solve second puzzle."""
    boss = load_boss(puzzle_input)
    combinations = get_combinations()

    combinations.sort(
        key=lambda items: sum(item[0] for item in items), reverse=True
    )

    for combination in combinations:
        if not play(combination, boss):
            return sum(item[0] for item in combination)

    return 0


@cache
def get_combinations():
    """Get all items combinations."""
    combinations = []

    for i, j, k, l in itertools.product(
        range(len(WEAPONS)),
        range(-1, len(ARMOR)),
        range(-1, len(RINGS)),
        range(-1, len(RINGS)),
    ):
        combination = [WEAPONS[i], (0, 0, 0), (0, 0, 0), (0, 0, 0)]

        if j >= 0:
            combination[1] = ARMOR[j]

        if k >= 0:
            combination[2] = RINGS[k]

        if l > k:
            combination[3] = RINGS[l]

        combinations.append(tuple(combination))

    return combinations


def load_boss(puzzle_input):
    """Load boss stats from input."""
    points = int(puzzle_input[0].split()[-1])
    damage = int(puzzle_input[1].split()[-1])
    armor = int(puzzle_input[2].split()[-1])

    return points, damage, armor


@cache
def play(items, boss):
    """Play a game."""
    player = [
        100,
        sum(item[1] for item in items),
        sum(item[2] for item in items),
    ]
    boss = list(boss)
    player_turn = True

    while player[0] > 0 and boss[0] > 0:
        if player_turn:
            boss[0] -= max(1, player[1] - boss[2])

        else:
            player[0] -= max(1, boss[1] - player[2])

        player_turn = not player_turn

    if player[0] <= 0:
        return False

    return True


if __name__ == "__main__":
    main()
