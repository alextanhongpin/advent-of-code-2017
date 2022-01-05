from collections import deque


def dance(n: int, moves: list[str], times=1) -> str:
    progs = deque([chr(i + ord("a")) for i in range(n)])

    movements = []
    for move in moves:
        match move[0]:
            case "s":
                movements.append(("s", int(move[1:])))
            case "x":
                a, b = [int(n) for n in move[1:].split("/")]
                movements.append(("x", a, b))
            case "p":
                a, b = [n for n in move[1:].split("/")]
                movements.append(("p", a, b))

    for i in range(times):
        for move in movements:
            match move:
                case ("s", a):
                    progs.rotate(a)
                case ("x", a, b):
                    progs[a], progs[b] = progs[b], progs[a]
                case ("p", a, b):
                    ai, bi = progs.index(a), progs.index(b)
                    progs[ai], progs[bi] = progs[bi], progs[ai]
    return "".join(progs)


with open("input.txt") as f:
    moves = f.read().strip().split(",")
    print("part 1:", dance(16, moves))
    # print("part 2:", dance(16, moves, times=1000000000))
    print("part 2:", dance(16, moves, times=1000))

