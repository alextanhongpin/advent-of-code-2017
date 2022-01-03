import re
from collections import defaultdict, Counter

prog = re.compile(r'\d+')


with open('input.txt') as f:
    lines = f.readlines()
    lines = sorted(lines, key=lambda x: len(x), reverse=True)
    towers = set()
    connections = set()
    towers_by_tower = defaultdict(set)

    weight_by_tower_name = {}
    for line in lines:
        name, *rest = line.split(' ')
        towers.add(name)
        weight = [int(n) for n in prog.findall(line)][0]
        weight_by_tower_name[name] = weight

    for line in lines:
        name, *rest = line.split(' ')
        if '->' in line:
            _, conns = line.split(' -> ')
            tower_connections = [conn.strip() for conn in conns.split(', ')]
            towers_by_tower[name].update(tower_connections)
            connections |= set(tower_connections)

    bottom = list((towers - connections))[0]
    print('part 1:', bottom)

    tower_and_connections = []
    q = [[bottom]]
    while q:
        towers = q.pop(0)
        new_towers = []
        for name in towers:
            new_towers.extend(towers_by_tower[name])
            tower_and_connections.append((name, towers_by_tower[name]))
        if len(new_towers) > 0:
            q.append(new_towers)

    # Update all tower weights, starting from bottom to top.
    for name, towers in reversed(tower_and_connections):
        total_weight = sum([weight_by_tower_name[tower_name] for tower_name in towers])
        weight_by_tower_name[name] += total_weight

    q = [(bottom, weight_by_tower_name[bottom])]
    while q:
        tower, target_weight = q.pop(0)
        weights = [weight_by_tower_name[name] for name in towers_by_tower[tower]]
        common_weights = Counter(sorted(weights)).most_common()
        if len(common_weights) > 1:
            for name in towers_by_tower[tower]:
                if weight_by_tower_name[name] == common_weights[-1][0]:
                    q.append((name, common_weights[0][0]))
        else:
            weight, freq = common_weights[0]
            print('part 2:', target_weight - weight * freq)
            break
