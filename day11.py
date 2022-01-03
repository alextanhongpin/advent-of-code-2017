def delta(direction: str) -> tuple[float, float]:
    match direction:
        case 'n':
            return (0, -1)
        case 's':
            return (0, 1)
        case 'ne':
            return (1, -0.5)
        case 'nw':
            return (-1, -0.5)
        case 'sw':
            return (-1, 0.5)
        case 'se':
            return (1, 0.5)
        case _:
            raise ValueError(f'Invalid direction: {dir}')


def hex_dist(point: tuple[int, int]) -> int:
    x, y = point
    x, y = abs(x), abs(y)
    steps = 0
    while x > 0:
        x -= 1
        y -= 0.5
        steps += 1
    while y > 0:
        y -= 1
        steps += 1
    return steps


with open('input.txt') as f:
    steps = f.read().strip().split(',')
    max_dist = 0
    point = [0, 0]
    for step in steps:
        x, y = point
        dx, dy = delta(step)
        point = (dx+x, dy+y)
        max_dist = max(max_dist, hex_dist(point))
    print('part 1:', hex_dist(point))
    print('part 2:', max_dist)
