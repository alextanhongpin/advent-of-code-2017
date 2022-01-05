import itertools

a, b = 703, 516
c, d = 16807, 48271
m = 2147483647
n = 2 ** 16 - 1

count = 0

for i in range(40_000_000):
    if i % 1_000_000 == 0:
        a *= c
        a %= m
        b *= d
        b %= m
    if a & n == b & n:
        print("found", count, i)
        count += 1

print(count)


def gen(start: int, constant: int, mod: int) -> int:
    while True:
        start *= constant
        start %= m
        if start % mod == 0:
            yield start


count = 0
for a, b in itertools.islice(zip(gen(a, c, 4), gen(b, d, 8)), 5_000_000):
    if a & n == b & n:
        count += 1

print(count)
