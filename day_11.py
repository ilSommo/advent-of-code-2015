"""Day 11: Corporate Policy"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools


def main():
    """Solve day 11 puzzles."""
    with open("data/day_11.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    numbers = str_to_list(puzzle_input)

    for i, number in enumerate(numbers):
        if number in [ord("i"), ord("o"), ord("l")]:
            numbers[i] += 1
            for j in range(i + 1, len(numbers)):
                numbers[j] = 97

    while not test_password(numbers):
        numbers = increase_password(numbers)

    string = list_to_str(numbers)

    return string


def star_2(puzzle_input):
    """Solve second puzzle."""
    string = star_1(puzzle_input)

    numbers = str_to_list(string)
    numbers = increase_password(numbers)
    string = list_to_str(numbers)

    string = star_1(string)

    return string


def increase_password(password):
    """Increase password value."""
    for i, number in enumerate(reversed(password)):
        if number in [ord("i") - 1, ord("o") - 1, ord("l") - 1]:
            password[-i - 1] += 2

            return password

        if number < 122:
            password[-i - 1] += 1

            return password

        password[-i - 1] = 97

    return password


def list_to_str(numbers):
    """Convert list of numbers to string."""
    string = "".join(chr(number) for number in numbers)

    return string


def str_to_list(string):
    """Convert string to list of numbers."""
    numbers = [ord(letter) for letter in string]

    return numbers


def test_password(password):
    """Test if password is valid."""
    if ord("i") in password or ord("o") in password or ord("l") in password:
        return 0

    if (
        sum(
            1 if len(list(g)) >= 2 else 0
            for _, g in itertools.groupby(password)
        )
        < 2
    ):
        return 0

    for i, _ in enumerate(password[:-2]):
        if (
            password[i + 1] - password[i]
            == password[i + 2] - password[i + 1]
            == 1
        ):
            return 1

    return 0


if __name__ == "__main__":
    main()
