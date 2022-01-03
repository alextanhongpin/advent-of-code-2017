valid = 0
with open('input.txt') as f:
    for line in f:
        words = line.strip().split(' ')
        if len(set(words)) == len(words):
            valid += 1

print('part 1:', valid)


def anagram(word: str) -> str:
    return ''.join(sorted(word))


valid = 0
with open('input.txt') as f:
    for line in f:
        words = line.strip().split(' ')
        words = [anagram(word) for word in words]
        if len(set(words)) == len(words):
            valid += 1

print('part 2:', valid)
