from collections import defaultdict


class Duet:
    def __init__(self, lines: list[str], prog_id: int):
        self.pos = 0
        self.lines = lines
        self.registers = defaultdict(int)
        self.registers["p"] = prog_id
        self.prog_id = prog_id
        self.received = []
        self.send = []
        self.sent = 0

    def parse(self, x: str) -> int:
        try:
            return int(x)
        except ValueError:
            return self.registers[x]

    def run(self) -> bool:
        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            match line:
                case ["snd", x]:
                    self.sent += 1
                    self.send.append(self.parse(x))
                case ["set", a, b]:
                    self.registers[a] = self.parse(b)
                case ["add", a, b]:
                    self.registers[a] += self.parse(b)
                case ["mul", a, b]:
                    self.registers[a] *= self.parse(b)
                case ["mod", a, b]:
                    self.registers[a] %= self.parse(b)
                case ["rcv", a]:
                    if not self.received:
                        return False
                    self.registers[a] = self.received.pop(0)
                case ["jgz", a, b]:
                    if self.parse(a) > 0:
                        self.pos += self.parse(b)
                        continue
            self.pos += 1
        return True


with open("input.txt") as f:
    lines = [line.strip().split(" ") for line in f]
    a, b = Duet(lines, prog_id=0), Duet(lines, prog_id=1)
    a_pos, b_pos = 0, 0
    part1 = False
    iters = 0
    while True:
        iters += 1
        a_done = a.run()
        b_done = b.run()
        if not part1:
            print("part 1:", a.send[-1])
            part1 = True
        if a.send and not b_done:
            b.received.append(a.send.pop(0))
        if b.send and not a_done:
            a.received.append(b.send.pop(0))
        if a.pos == a_pos and b.pos == b_pos and not a.received and not b.received:
            print("deadlock")
            break
        a_pos = a.pos
        b_pos = b.pos
    print("part 2:", b.sent)
    # print(a.registers)
    # print(b.registers)
