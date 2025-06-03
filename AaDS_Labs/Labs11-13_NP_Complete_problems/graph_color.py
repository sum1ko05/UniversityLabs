from itertools import product


def is_valid_color(graph, colors):
    for vertex in graph:
        for neighbor in graph[vertex]: # Only different vertices since graph don't contain 1-vertex cycles
            if colors[vertex] == colors[neighbor]:
                return False
    return True


def graph_coloring_brute_force(graph, max_colors):
    vertices = list(graph.keys())
    n = len(vertices)

    for coloring in product(range(1, max_colors + 1), repeat=n):
        colors = dict(zip(vertices, coloring))
        if is_valid_color(graph, colors):
            return colors
    return None


def min_colors(graph):
    chromatic_number = 1
    while True:
        coloring = graph_coloring_brute_force(graph, chromatic_number)
        if coloring is not None:
            return chromatic_number, coloring
        chromatic_number += 1
