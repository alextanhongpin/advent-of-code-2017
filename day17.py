from collections import deque


steps = 371


def spin(insertions: int, steps: int, target: int) -> int:
    spinlock = deque([0])
    for i in range(1, insertions + 1):
        spinlock.rotate(-steps)
        spinlock.append(i)
    tgt = spinlock.index(target)
    spinlock.rotate(tgt + 1)
    return spinlock[0]


print(spin(2017, steps, 2017))


# 0 stays at the same position, so we only check any item that is placed after
# it
curr = 0
length = 1
last = 0
for i in range(50000000):
    curr = (curr + steps) % length
    curr += 1
    if curr == 1:
        last = i
    length += 1


print(last)
