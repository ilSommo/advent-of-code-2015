"""Day 4: The Ideal Stocking Stuffer"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import hashlib


def main():
    """Solve day 4 puzzles"""
    with open("data/day_4.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle"""
    answer = 0

    while not (
        hashlib.md5(f"{puzzle_input}{answer}".encode())
        .hexdigest()
        .startswith(5 * "0")
    ):
        answer += 1

    return answer


def star_2(puzzle_input):
    """Solve second puzzle"""
    answer = 0

    while not (
        hashlib.md5(f"{puzzle_input}{answer}".encode())
        .hexdigest()
        .startswith(6 * "0")
    ):
        answer += 1

    return answer


if __name__ == "__main__":
    main()
