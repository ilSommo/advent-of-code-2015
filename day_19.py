"""Day 19: Medicine for Rudolph"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from functools import cache
import re


def main():
    """Solve day 19 puzzles."""
    with open("data/day_19.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    substitutions, molecule = parse_input(puzzle_input)
    molecules = set()

    for k, v in substitutions:
        for index in re.finditer(k, molecule):
            i, j = index.start(), index.end()
            molecules.add(molecule[:i] + v + molecule[j:])

    n_molecules = len(molecules)

    return n_molecules


def star_2(puzzle_input):
    """Solve second puzzle."""
    substitutions, molecule = parse_input(puzzle_input)
    steps = 0

    while molecule != "e":
        steps += 1
        for k, v in substitutions:
            if v in molecule:
                molecule = molecule.replace(v, k, 1)
                break

    return steps


@cache
def parse_input(puzzle_input):
    """Parse input file."""
    substitutions = tuple(
        sorted(
            [line.split(" => ") for line in puzzle_input[:-2]],
            key=lambda elem: len(elem[1]),
            reverse=True,
        )
    )

    molecule = puzzle_input[-1]

    return substitutions, molecule


if __name__ == "__main__":
    main()
