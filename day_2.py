"""Day 2: I Was Told There Would Be No Math"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"


def main():
    """Solve day 2 puzzles"""
    with open("data/day_2.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle"""
    paper = 0

    for present in puzzle_input:
        d0, d1, d2 = get_dimensions(present)
        paper += 3 * d0 * d1 + 2 * d2 * (d0 + d1)

    return paper


def star_2(puzzle_input):
    """Solve second puzzle"""
    ribbon = 0

    for present in puzzle_input:
        d0, d1, d2 = get_dimensions(present)
        ribbon += 2 * (d0 + d1) + d0 * d1 * d2

    return ribbon


def get_dimensions(present):
    """Get sorted dimensions of present"""
    d0, d1, d2 = tuple(sorted(int(dim) for dim in present.split("x")[:3]))

    return d0, d1, d2


if __name__ == "__main__":
    main()
