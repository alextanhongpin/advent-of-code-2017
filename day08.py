from collections import defaultdict


with open('input.txt') as f:
    reg = defaultdict(int)
    max_val = 0
    for line in f:
        line = line.strip()
        a, op, n, _, b, token, c = line.split(' ')
        cond = False
        match token:
            case '>':
                cond = reg[b] > int(c)
            case '<':
                cond = reg[b] < int(c)
            case '==':
                cond = reg[b] == int(c)
            case '<=':
                cond = reg[b] <= int(c)
            case '>=':
                cond = reg[b] >= int(c)
            case '!=':
                cond = reg[b] != int(c)
            case _:
                raise ValueError(f'Unknown token {token}')
        if not cond:
            continue
        match op:
            case 'inc':
                reg[a] += int(n)
            case 'dec':
                reg[a] -= int(n)
            case _:
                raise ValueError(f'Unknown op {op}')
        max_val = max(max_val, max(reg.values()))
    print('part 1:', max(reg.values()))
    print('part 2:', max_val)
