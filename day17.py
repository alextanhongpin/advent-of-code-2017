from collections import deque


steps = 371


def spin(insertions: int, steps: int, target: int) -> int:
    spinlock = deque([0])
    for i in range(1, insertions + 1):
        spinlock.rotate(-steps)
        spinlock.append(i)
    while spinlock[0] != target:
        spinlock.rotate(1)
    spinlock.rotate(-1)
    return spinlock[0]


print(spin(2017, steps, 2017))
print(spin(50000000, steps, 0))
