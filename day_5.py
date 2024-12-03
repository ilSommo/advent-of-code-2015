"""Day 5: Doesn't He Have Intern-Elves For This?"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import re


def main():
    """Solve day 5 puzzles."""
    with open("data/day_5.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle"""
    nice_strings = sum(check_niceness(line) for line in puzzle_input)

    return nice_strings


def star_2(puzzle_input):
    """Solve second puzzle."""
    nice_strings = sum(check_niceness_2(line) for line in puzzle_input)

    return nice_strings


def check_niceness(string):
    """Check string niceness."""
    if (
        len(re.findall(r"[aeiou]", string)) >= 3
        and len(re.findall(r"(.)\1", string)) >= 1
        and len(re.findall(r"ab|cd|pq|xy", string)) == 0
    ):
        return 1

    return 0


def check_niceness_2(string):
    """Check string niceness."""
    if (
        len(re.findall(r"(..).*\1", string)) >= 1
        and len(re.findall(r"(.).\1", string)) >= 1
    ):
        return 1

    return 0


if __name__ == "__main__":
    main()
