from functools import reduce


def knot_hash(nums: list[int], lengths: list[int], rounds: int = 1) -> list[int]:
    current_position, skip_size = 0, 0
    for _ in range(rounds):
        for n in lengths:
            for i in range(n // 2):
                (
                    nums[(current_position + i) % len(nums)],
                    nums[(current_position + n - 1 - i) % len(nums)],
                ) = (
                    nums[(current_position + n - 1 - i) % len(nums)],
                    nums[(current_position + i) % len(nums)],
                )
            current_position = (current_position + n + skip_size) % len(nums)
            skip_size += 1

    return nums


nums = list(range(256))
lengths = [225, 171, 131, 2, 35, 5, 0, 13, 1, 246, 54, 97, 255, 98, 254, 110]
h = knot_hash(nums, lengths, rounds=1)
print("part 1:", h[0] * h[1])

inp = "225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110"
nums = list(range(256))
lengths = [ord(ch) for ch in inp] + [17, 31, 73, 47, 23]
sparse_hash = knot_hash(nums, lengths, rounds=64)
dense_hash = [
    reduce(lambda x, y: x ^ y, sparse_hash[i * 16 : (i + 1) * 16]) for i in range(16)
]
for n in dense_hash:
    if n < 10:
        print(0, end="")
        print(n, end="")
    else:
        print(hex(n)[2:], end="")
