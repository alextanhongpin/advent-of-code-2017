cache = set()
banks = [int(bank) for bank in '14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4'.split('\t')]
print(banks)
steps = 0

while True:
    key = tuple(banks)
    if key in cache:
        break
    cache.add(key)

    steps += 1
    n = max(banks)
    ni = banks.index(n)
    banks[ni] = 0
    for i in range(n):
        banks[(ni + i + 1) % len(banks)] += 1

print('part 1:', steps)

last_steps = steps
cache.clear()
while True:
    key = tuple(banks)
    if key in cache:
        break
    cache.add(key)

    steps += 1
    n = max(banks)
    ni = banks.index(n)
    banks[ni] = 0
    for i in range(n):
        banks[(ni + i + 1) % len(banks)] += 1

print('part 2:', steps-last_steps)
