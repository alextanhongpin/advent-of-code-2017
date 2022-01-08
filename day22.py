import copy
from collections import defaultdict


def turn_right(direction: complex) -> complex:
    return direction * -1j


def turn_left(direction: complex) -> complex:
    return direction * 1j


def reverse(direction: complex) -> complex:
    return turn_right(turn_right(direction))


with open("input.txt") as f:
    nodes = defaultdict(int)
    lines = f.readlines()
    for y, line in enumerate(lines):
        row = line.strip()
        for x, ch in enumerate(row):
            if ch == "#":
                nodes[complex(x - len(row) // 2, len(lines) // 2 - y)] = 1

    evolved = defaultdict(int)
    for key in nodes:
        evolved[key] = 2

    direction = 0 + 1j  # Up
    pos = 0 + 0j
    bursts = 10000
    infected = 0

    for i in range(bursts):
        curr = nodes[pos]
        direction = turn_right(direction) if curr == 1 else turn_left(direction)
        if curr == 0:
            infected += 1
        nodes[pos] = (curr + 1) % 2
        pos += 1 * direction
    print("part 1:", infected)

    direction = 0 + 1j  # Up
    pos = 0 + 0j
    bursts = 10000000
    infected = 0

    for i in range(bursts):
        curr = evolved[pos]
        match curr:
            case 0:
                direction = turn_left(direction)
            case 1:
                infected += 1
            case 2:
                direction = turn_right(direction)
            case 3:
                direction = reverse(direction)
        evolved[pos] = (curr + 1) % 4
        pos += 1 * direction

    print("part 2:", infected)
