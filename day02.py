part1 = 0
part2 = 0

with open('input.txt', 'r') as f:
    for line in f:
        nums = [int(n) for n in line.strip().split('\t')]
        part1 += max(nums) - min(nums)

        sorted_nums = sorted(nums)
        for i, a in enumerate(sorted_nums):
            for b in sorted_nums[i+1:]:
                if b // a * a == b:
                    part2 += b // a


print('part 1:', part1)
print('part 2:', part2)
