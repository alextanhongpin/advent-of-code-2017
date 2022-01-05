def parse(input_file: str) -> list[int, int]:
    """
    Parses the input file and returns a list of instructions.
    """
    with open(input_file, 'r') as f:
        result = []
        for line in f:
            layer, depth = [int(n) for n in line.strip().split(': ')]
            result.append([layer, depth])
        return result

Layer = tuple[int, int]

def scanner(n: int, t: int) -> int:
    cycle = n * 2 - 2
    pos = t % cycle
    offset = 0
    if pos > n - 1:
        pos = 2 * n - pos - 2
    return pos


def simulate(layers: list[Layer]) -> tuple[int]:
    """
    Simulates the firewall.
    """
    severity = 0
    for (layer, depth) in layers:
        if scanner(depth, layer) == 0:
            severity += layer * depth
    return severity

def check_caught(layers: list[Layer], delay=0) -> tuple[bool]:
    for (layer, depth) in layers:
        if scanner(depth, layer+delay) == 0:
            return True
    return False

print('part 1:', simulate(parse('input.txt')))
caught = True
delay = 0
while check_caught(parse('input.txt'), delay=delay):
    print(delay)
    delay += 1
print('part 2:', delay)
