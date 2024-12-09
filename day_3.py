"""Day 3: Perfectly Spherical Houses in a Vacuum"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

CHAR_TO_COMPLEX = {"^": 0 + 1j, "v": 0 - 1j, ">": 1 + 0j, "<": -1 + 0j}


def main():
    """Solve day 3 puzzles."""
    with open("data/day_3.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    locations = {0 + 0j}
    santa = 0 + 0j

    for move in puzzle_input:
        santa += CHAR_TO_COMPLEX[move]
        locations.add(santa)

    return len(locations)


def star_2(puzzle_input):
    """Solve second puzzle."""
    locations = {0 + 0j}
    santa = 0 + 0j
    robo_santa = 0 + 0j

    for i, move in enumerate(puzzle_input):
        if i % 2 == 0:
            santa += CHAR_TO_COMPLEX[move]
            locations.add(santa)

        else:
            robo_santa += CHAR_TO_COMPLEX[move]
            locations.add(robo_santa)

    return len(locations)


if __name__ == "__main__":
    main()
