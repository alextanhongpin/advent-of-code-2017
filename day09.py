def count_curly_brackets(inp: str) -> tuple[int, int]:
    tokens = []
    garbage = []
    ignore = []
    inner = 0
    score = 0
    non_cancelled_garbage = 0

    for ch in inp:
        if ignore:
            ignore.pop()
            continue

        if garbage:
            match ch:
                case '>':
                    garbage.pop()
                case '!':
                    ignore.append(ch)
                case _:
                    non_cancelled_garbage += 1
        else:
            if ch == '{':
                inner += 1
                tokens.append(ch)
            elif ch == '}':
                while tokens and tokens[-1] != '{':
                    tokens.pop()
                tokens.pop()
                score += inner
                inner -= 1
            elif ch == '!':
                ignore.append(ch)
            elif ch == '<':
                garbage.append(ch)

    return score, non_cancelled_garbage

with open('input.txt', 'r') as f:
    inp = f.read()
    print(count_curly_brackets(inp))
