from math import inf


def remove_units(line):
    changed = True
    while changed:
        for i in range(len(line)):
            if (i + 1) >= len(line):
                continue
            curr_char = line[i]
            next_char = line[i + 1]
            if curr_char.islower():
                if next_char.isupper() and next_char.lower() == curr_char:
                    line[i] = '_'
                    line[i + 1] = '_'
            else:
                if next_char.islower() and next_char.upper() == curr_char:
                    line[i] = '_'
                    line[i + 1] = '_'
        if '_' not in line:
            changed = False
        line = list(filter(lambda c: c != '_', line))
    return len(line)


def part1(line):
    return remove_units(list(line))


def part2(line):
    min_length = inf
    for char in set(line.lower()):
        length = remove_units(list(filter(lambda c: c != char and c.lower() != char, line)))
        if length < min_length:
            min_length = length
    return min_length


if __name__ == '__main__':
    line = []
    with open('inputs/05') as f:
        line = f.readline().rstrip('\n')
    print(part1(line))
    print(part2(line))
