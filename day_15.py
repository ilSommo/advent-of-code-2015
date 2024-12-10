"""Day 15: Science for Hungry People"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"


def main():
    """Solve day 15 puzzles."""
    with open("data/day_15.txt", encoding="ascii") as input_file:
        puzzle_input = [line.rstrip() for line in input_file.readlines()]

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    ingredients = get_ingredients(puzzle_input)
    scores = []

    for i in range(98):
        for j in range(98 - i):
            for k in range(98 - i - j):
                l = 100 - i - j - k
                scores.append(compute_score(ingredients, (i, j, k, l)))

    max_score = max(scores)

    return max_score


def star_2(puzzle_input):
    """Solve second puzzle."""
    ingredients = get_ingredients(puzzle_input)
    scores = []

    for i in range(98):
        for j in range(98 - i):
            for k in range(98 - i - j):
                l = 100 - i - j - k
                if (
                    sum(
                        quantity * ingredients[index][-1]
                        for index, quantity in enumerate((i, j, k, l))
                    )
                    == 500
                ):
                    scores.append(compute_score(ingredients, (i, j, k, l)))

    max_score = max(scores)

    return max_score


def compute_score(ingredients, quantities):
    """Compute scores for given ingredients and quantities."""
    score = 1
    property_scores = []

    for property_, _ in enumerate(ingredients[0][:-1]):
        property_scores.append(
            sum(
                quantities[i] * ingredient[property_]
                for i, ingredient in enumerate(ingredients)
            )
        )

    for property_score in property_scores:
        score *= max(property_score, 0)

    return score


def get_ingredients(puzzle_input):
    """Get ingredients from puzzle input."""
    ingredients = tuple(
        tuple(
            int(property_)
            for property_ in (
                line.split()[2][:-1],
                line.split()[4][:-1],
                line.split()[6][:-1],
                line.split()[8][:-1],
                line.split()[10],
            )
        )
        for line in puzzle_input
    )

    return ingredients


if __name__ == "__main__":
    main()
