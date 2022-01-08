import re

from collections import defaultdict

prog = re.compile(r"\d+")


with open("input.txt") as f:
    lines = f.readlines()
    init = None
    steps = 0
    values = defaultdict(int)
    state = None
    tapes = {}

    while lines:
        line = lines.pop(0)
        line = line.strip().replace(".", "").replace(":", "")
        if line == "":
            state = None
            continue

        if line.startswith("Begin"):
            init = line.split(" ")[-1]
        elif line.startswith("Perform"):
            steps = [int(n) for n in prog.findall(line)][0]
        elif line.startswith("In"):
            state = line.split(" ")[-1]
        elif line.startswith("If"):
            value = int(line.split(" ")[-1])
            write = [int(n) for n in prog.findall(lines.pop(0).strip())][0]
            slot = 1 if "right" in lines.pop(0).strip() else -1
            next_state = lines.pop(0).strip().split(" ")[-1][:-1]
            if state not in tapes:
                tapes[state] = defaultdict(dict)
            tapes[state][value] = (write, slot, next_state)

    pos = 0
    while steps > 0:
        write, slot, next_state = tapes[state][values[pos]]
        values[pos] = write
        pos += slot
        state = next_state
        steps -= 1
    print(sum(values.values()))
