from collections import Counter


def flatten(items: list[list[int]]) -> list[int]:
    return [item for sublist in items for item in sublist]


with open("input.txt") as f:
    pins = []
    start = []
    for line in f:
        pin = [int(n) for n in line.strip().split("/")]
        if line.startswith("0"):
            start.append(pin)
        else:
            pins.append(pin)

    start = [[pin] for pin in start]
    combinations = []
    while start:
        pin = start.pop(0)

        for other in pins:
            if other in pin:
                continue
            ports = set(other) & set(pin[-1])
            if not ports:
                continue
            new_pin = pin + [other]

            counter = Counter(flatten(new_pin))
            single = 0
            for k, v in counter.items():
                if v % 2 == 1:
                    single += 1
            if single == 2:
                start.append(new_pin)
                combinations.append(new_pin)
        combinations.append(pin)

    scores = [(len(com), sum(flatten(com)), com) for com in combinations]
    strongest = sorted(scores, key=lambda x: x[1], reverse=True)[0]
    longest = sorted(scores, key=lambda x: (x[0], x[1]), reverse=True)[0]
    print("part 1:", strongest[1])
    print("part 2:", longest[1])
