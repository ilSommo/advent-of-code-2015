"""Day 24: It Hangs in the Balance"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools
import math


def main():
    """Solve day 24 puzzles."""
    with open("data/day_24.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    packages = load_packages(puzzle_input)
    weight = sum(packages) / 3

    combinations = create_combinations(packages, weight)
    combinations.sort(key=math.prod)

    return math.prod(combinations[0])


def star_2(puzzle_input):
    """Solve second puzzle."""
    packages = load_packages(puzzle_input)
    weight = sum(packages) / 4

    combinations = create_combinations(packages, weight)
    combinations.sort(key=math.prod)

    return math.prod(combinations[0])


def create_combinations(packages, weight):
    """Create all possible combinations with same weight and minimal passenger packages."""
    packages = packages[::-1]
    combinations = []

    for len_passenger, _ in enumerate(packages):
        for passenger_packages in itertools.combinations(
            packages, len_passenger
        ):
            if sum(passenger_packages) == weight:
                combinations.append(passenger_packages)

        if combinations:
            break

    return combinations


def load_packages(puzzle_input):
    """Load packages from input."""
    return tuple(int(line) for line in puzzle_input)


if __name__ == "__main__":
    main()
