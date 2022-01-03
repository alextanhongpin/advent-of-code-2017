import math

# bound = int(math.sqrt(368078)+1)
# x = bound // 2 - (bound ** 2 - 368078)
# y = bound // 2
# dist = abs(x) + abs(y)
# print(dist)

origin = (0, 0)

points = {}
points[origin] = 1
div = 1
val = 1

TARGET = 368078

directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
while True:
    div += 2
    new_points = div ** 2 - (div - 2) ** 2
    steps = new_points//4

    # Start at the origin x + 1, y + 1, move up, left, down and right the
    # number of steps
    origin = (origin[0] + 1, origin[1] + 1)
    for n in range(new_points):
        dx, dy = directions[n // steps]
        if val == TARGET:
            print('part 1:', abs(origin[0]) + abs(origin[1]))
            break
        origin = (origin[0] + dx, origin[1] + dy)
        val += 1
        points[origin] = val
    else:
        continue
    break

origin = (0, 0)

points = {}
points[origin] = 1
div = 1

TARGET = 368078

directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
neighbours = [(-1, -1), (0, -1), (1, -1),
              (-1, 0), (1, 0),
              (-1, 1), (0, 1), (1, 1)]

while True:
    div += 2
    new_points = div ** 2 - (div - 2) ** 2
    steps = new_points//4
    origin = (origin[0] + 1, origin[1] + 1)
    for n in range(new_points):
        dx, dy = directions[n // steps]
        origin = (origin[0] + dx, origin[1] + dy)
        val = 0
        for nx, ny in neighbours:
            val += points.get((origin[0] + nx, origin[1] + ny), 0)
        if val >= TARGET:
            print('part 2:', val)
            break
        points[origin] = val
    else:
        continue
    break
