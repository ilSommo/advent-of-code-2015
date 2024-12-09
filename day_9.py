"""Day 9: All in a Single Night"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools
from collections import defaultdict


def main():
    """Solve day 9 puzzles."""
    with open("data/day_9.txt", encoding="ascii") as input_file:
        puzzle_input = [line.rstrip() for line in input_file.readlines()]

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    graph = load_graph(puzzle_input)
    distances = compute_distances(graph)

    return min(distances)


def star_2(puzzle_input):
    """Solve second puzzle."""
    graph = load_graph(puzzle_input)
    distances = compute_distances(graph)

    return max(distances)


def compute_distances(graph):
    """Compute all possible distances."""
    distances = []

    for edge in graph.keys():
        for path in itertools.permutations(graph.keys() - {edge}):
            path = [edge] + list(path)
            distances.append(
                sum(
                    graph[path[i]][path[i + 1]]
                    for i, _ in enumerate(path[:-1])
                )
            )

    return distances


def load_graph(puzzle_input):
    """Load graph from puzzle input."""
    graph = defaultdict(dict)

    for line in puzzle_input:
        node_0, _, node_1, _, edge = line.split()
        graph[node_0][node_1] = int(edge)
        graph[node_1][node_0] = int(edge)

    return dict(graph)


if __name__ == "__main__":
    main()
