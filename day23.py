from collections import defaultdict


class Duet:
    def __init__(self, lines: list[str], debug=False):
        self.pos = 0
        self.lines = lines
        self.registers = defaultdict(int)
        if debug:
            self.registers["a"] = 1
        self.count = defaultdict(int)

    def parse(self, x: str) -> int:
        try:
            return int(x)
        except ValueError:
            return self.registers[x]

    def run(self) -> bool:
        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            self.count[line[0]] += 1
            match line:
                case ["set", a, b]:
                    self.registers[a] = self.parse(b)
                case ["add", a, b]:
                    self.registers[a] += self.parse(b)
                case ["sub", a, b]:
                    self.registers[a] -= self.parse(b)
                case ["mul", a, b]:
                    self.registers[a] *= self.parse(b)
                case ["mod", a, b]:
                    self.registers[a] %= self.parse(b)
                case ["jnz", a, b]:
                    if self.parse(a) != 0:
                        self.pos += self.parse(b)
                        continue
            self.pos += 1
        return True


with open("input.txt") as f:
    lines = [line.strip().split(" ") for line in f]
    duet = Duet(lines)
    duet.run()
    print("part 1:", duet.count["mul"])

    non_primes = 0

    print("part 1:", (81 - 2) ** 2)
    x = 81 * 100 + 100000

    for n in range(x, x + 17_000 + 1, 17):
        d = 2
        while n % d != 0:
            d += 1
        if n != d:
            non_primes += 1
    print("part 2:", non_primes)
