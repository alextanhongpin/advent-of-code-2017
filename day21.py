import math
from functools import partial


def parse(inp: str) -> list[list[str]]:
    return [[x for x in line] for line in inp.split("/")]


def to_str(items: list[list[str]]) -> str:
    return "/".join(["".join(item) for item in items])


def rotate(matrix, n=0):
    for i in range(n):
        matrix = list(zip(*reversed(matrix)))
    return matrix


def flip(matrix, axis=0):
    if axis == 0:
        return list(reversed(matrix))
    elif axis == 1:
        return [list(reversed(x)) for x in matrix]
    else:
        raise ValueError("Invalid axis")


def new_matrix(m: int) -> list[list[str]]:
    return [[None for _ in range(m)] for _ in range(m)]


def fractal(square: list[list[str]]) -> list[list[str]]:
    n = len(square)
    if n % 2 == 0:
        m = n // 2 * 3
        new_square = new_matrix(m)
        y0 = 0
        for y in range(0, n, 2):
            x0 = 0
            for x in range(0, n, 2):
                part = [row[x : x + 2] for row in square[y : y + 2]]
                repl = parse(transform[to_str(part)])

                for j, row in enumerate(repl):
                    new_square[y + y0 + j][x + x0 : x + x0 + 4] = row
                x0 += 1
            y0 += 1
    elif n % 3 == 0:
        m = n // 3 * 4
        new_square = new_matrix(m)
        y0 = 0
        for y in range(0, n, 3):
            x0 = 0
            for x in range(0, n, 3):
                part = [row[x : x + 3] for row in square[y : y + 3]]
                repl = parse(transform[to_str(part)])

                for j, row in enumerate(repl):
                    new_square[y + y0 + j][x + x0 : x + x0 + 4] = row
                x0 += 1
            y0 += 1
    return new_square


start = ".#./..#/###"


with open("input.txt") as f:
    transform = {}
    rotations = [
        partial(rotate, n=0),
        partial(rotate, n=1),
        partial(rotate, n=2),
        partial(rotate, n=3),
    ]

    for line in f:
        src, tgt = line.strip().split(" => ")
        parsed = parse(src)
        for tr in rotations:
            transform[to_str(tr(parsed))] = tgt
            transform[to_str(tr(flip(parsed, axis=0)))] = tgt
            transform[to_str(tr(flip(parsed, axis=1)))] = tgt

    square = parse(start)
    rounds = 5
    for _ in range(rounds):
        square = fractal(square)
    print("part 1:", sum([1 if col == "#" else 0 for row in square for col in row]))

    square = parse(start)
    rounds = 18

    squares = [square]
    cache = {}

    # Based on the hint on Reddit, after 3 iterations, 9 squares will be
    # produced, and can be used to calculate further squares independently.
    for _ in range(rounds // 3):
        new_squares = []
        for square in squares:
            key = to_str(square)
            if key in cache:
                new_squares.extend(cache[key])
            else:
                for _ in range(3):
                    square = fractal(square)
                n = len(square)
                result = []
                for y in range(0, n, 3):
                    for x in range(0, n, 3):
                        part = [row[x : x + 3] for row in square[y : y + 3]]
                        result.append(part)
                cache[key] = result
                new_squares.extend(result)
        squares = new_squares

    print(
        "part 2:",
        sum(
            [
                1 if col == "#" else 0
                for square in squares
                for row in square
                for col in row
            ]
        ),
    )
