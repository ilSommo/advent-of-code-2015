"""Day 20: Infinite Elves and Infinite Houses"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools
from functools import cache


def main():
    """Solve day 20 puzzles."""
    with open("data/day_20.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    house = 0

    while True:
        house += 1
        presents = sum(10 * i for i in factorize(house))

        if presents >= int(puzzle_input):
            break

    return house


def star_2(puzzle_input):
    """Solve second puzzle."""
    house = 0

    while True:
        house += 1
        presents = sum(11 * i for i in factorize(house) if house / i < 51)

        if presents >= int(puzzle_input):
            break

    return house


def get_prime_powers(n):
    """Get prime powers of a number."""
    for c in itertools.accumulate(
        itertools.chain((2, 1, 2), itertools.cycle((2, 4)))
    ):
        if c * c > n:
            break

        if n % c:
            continue

        d, p = (), c

        while not n % c:
            n, p, d = n // c, p * c, d + (p,)

        yield d

    if n > 1:
        yield (n,)


@cache
def factorize(n):
    """Factorize a number."""
    r = [1]

    for e in get_prime_powers(n):
        r += [a * b for a in r for b in e]

    return r


if __name__ == "__main__":
    main()
