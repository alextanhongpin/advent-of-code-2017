with open("input.txt") as f:
    position = None
    grid = {}
    for y, line in enumerate(f.readlines()):
        for x, char in enumerate(line.rstrip()):
            if char.strip() != "":
                grid[complex(x, y)] = char
                if y == 0:
                    position = complex(x, y)

    collection = ""
    direction = 0 + 1j  # South
    steps = 1
    while position in grid:
        position += direction
        if position not in grid:
            break
        steps += 1
        curr = grid[position]
        if curr.isalpha():
            collection += curr
        elif curr == "+":
            if (position + (direction * -1j)) in grid:
                direction = direction * -1j
            elif (position + (direction * 1j)) in grid:
                direction = direction * 1j

    print("part 1:", collection)
    print("part 2:", steps)
