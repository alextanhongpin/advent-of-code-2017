with open('input.txt') as f:
    num = [int(line.strip()) for line in f]
    reg = num.copy()

    i = 0
    steps = 0
    while i < len(reg):
        steps += 1
        ni = i + reg[i]
        reg[i] += 1
        i = ni
    print('part 1:', steps)


    reg = num.copy()
    i = 0
    steps = 0
    while i < len(reg):
        steps += 1
        ni = i + reg[i]
        reg[i] += 1 if reg[i] < 3 else -1
        i = ni
    print('part 2:', steps)
