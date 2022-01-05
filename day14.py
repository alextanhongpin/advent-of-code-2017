from functools import reduce


def knot_hash(inp: str, rounds: int = 64) -> str:
    sparse_hash = list(range(256))
    lengths = [ord(ch) for ch in inp] + [17, 31, 73, 47, 23]
    current_position, skip_size = 0, 0
    for _ in range(rounds):
        for n in lengths:
            for i in range(n // 2):
                (
                    sparse_hash[(current_position + i) % len(sparse_hash)],
                    sparse_hash[(current_position + n - 1 - i) % len(sparse_hash)],
                ) = (
                    sparse_hash[(current_position + n - 1 - i) % len(sparse_hash)],
                    sparse_hash[(current_position + i) % len(sparse_hash)],
                )
            current_position = (current_position + n + skip_size) % len(sparse_hash)
            skip_size += 1

    dense_hash = [
        reduce(lambda x, y: x ^ y, sparse_hash[i * 16 : (i + 1) * 16])
        for i in range(16)
    ]

    return "".join(f"{x:02x}" for x in dense_hash)


q = set()
grid = {}
key = "hfdlxzhv"
total = 0
for y in range(128):
    h = knot_hash(f"{key}-{y}")
    b = f"{int(h, 16):0128b}"
    total += sum(map(int, b))
    for x, v in enumerate(b):
        p, n = (x, y), int(v)
        grid[p] = n
        if n == 1:
            q.add(p)


print("part 1:", total)

Point = tuple[int, int]


def bfs(start: Point, grid: dict[Point, int]) -> set[Point]:
    q = set([start])
    visited = set()
    neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while q:
        p = q.pop()
        if p in visited:
            continue
        visited.add(p)

        for dx, dy in neighbors:
            x, y = p
            dx += x
            dy += y
            if (dx, dy) in grid and grid[(dx, dy)] == 1:
                q.add((dx, dy))
    return visited


region = 0
while q:
    start = q.pop()
    visited = bfs(start, grid)
    region += 1
    q -= visited


print("part 2:", region)
