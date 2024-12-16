"""Day 17: No Such Thing as Too Much"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools


def main():
    """Solve day 17 puzzles."""
    with open("data/day_17.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    containers = tuple(int(line) for line in puzzle_input)

    return sum(
        sum(containers_combination) == 150
        for i in range(len(puzzle_input))
        for containers_combination in itertools.combinations(containers, i)
    )


def star_2(puzzle_input):
    """Solve second puzzle."""
    containers = tuple(int(line) for line in puzzle_input)

    combinations = tuple(
        len(containers_combination)
        for i in range(len(puzzle_input))
        for containers_combination in itertools.combinations(containers, i)
        if sum(containers_combination) == 150
    )

    return combinations.count(min(combinations))


if __name__ == "__main__":
    main()
