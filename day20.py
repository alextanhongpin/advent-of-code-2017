# TODO: Revisit, got lucky

import re
from collections import defaultdict

prog = re.compile(r"-?\d+")


with open("input.txt") as f:
    particles = []
    for id, line in enumerate(f.readlines()):
        particle = (id, [int(n) for n in prog.findall(line)])
        particles.append(particle)

    def update(particle: tuple[int, list[int]], c: int = 1) -> tuple[int, list[int]]:
        (id, [dx, dy, dz, vx, vy, vz, ax, ay, az]) = particle
        vx += ax * c
        vy += ay * c
        vz += az * c
        dx += vx
        dy += vy
        dz += vz
        return id, [dx, dy, dz, vx, vy, vz, ax, ay, az]

    def distance(particle):
        (_, [dx, dy, dz, *rest]) = particle
        return abs(dx) + abs(dy) + abs(dz)

    # Assign a constant that magnifies the acceleration of the particles.
    particles0 = [update(p, 10 ** 5) for p in particles[:]]
    particles0 = sorted(particles0, key=distance)
    print("part 1:", particles0[0][0])

    iters = 0
    while True:
        iters += 1
        positions = defaultdict(list)
        for p in particles:
            p = update(p)
            positions[tuple(p[1][:3])].append(p)

        keys = list(positions.keys())
        for p in keys:
            if len(positions[p]) > 1:
                del positions[p]
        particles = [p[0] for p in positions.values()]
        if iters > 10000:
            break
    print("part 2:", len(particles))
