"""Day 10: Elves Look, Elves Say"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools


def main():
    """Solve day 10 puzzles."""
    with open("data/day_10.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    sequence = puzzle_input

    for _ in range(40):
        sequence = look_and_say(sequence)

    return len(sequence)


def star_2(puzzle_input):
    """Solve second puzzle."""
    sequence = puzzle_input

    for _ in range(50):
        sequence = look_and_say(sequence)

    return len(sequence)


def look_and_say(sequence):
    new_sequence = "".join(
        f"{len(list(g))}{k}" for k, g in itertools.groupby(sequence)
    )

    return new_sequence


if __name__ == "__main__":
    main()
