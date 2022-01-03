Program = tuple[int, set[int]]


def find_groups(programs: list[Program], n: int) -> set[int]:
    contains = set([n])
    while True:
        n = len(contains)
        for i, progs in programs:
            if i in contains:
                contains |= progs
            if contains & progs:
                contains.add(i)
        if n == len(contains):
            return contains


with open("input.txt") as f:
    programs = []
    for line in f:
        prog, rest = line.split(" <-> ")
        progi = int(prog)
        progs = {int(n) for n in rest.split(", ")}
        programs.append((progi, progs))

    groups = 1
    contains_zero = find_groups(programs, 0)
    grouped = contains_zero.copy()
    while True:
        remaining = set([id for id, _ in programs]) - grouped
        if not remaining:
            break
        remaining_progs = [progs for progs in programs if progs[0] in remaining]
        new_grouped = find_groups(remaining_progs, list(remaining)[0])
        grouped |= new_grouped
        groups += 1

    print("part 1:", len(contains_zero))
    print("part 2:", groups)
