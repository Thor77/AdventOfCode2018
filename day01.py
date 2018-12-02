from time import time


def part1(changes):
    return sum(changes)


def part2(changes):
    frequencies = set()
    result = 0
    while True:
        for change in changes:
            result += change
            if result in frequencies:
                return result
            else:
                frequencies.add(result)


if __name__ == '__main__':
    changes = []
    with open('inputs/01') as f:
        changes = list(map(int, filter(None, f.readlines())))
    print(part1(changes))
    times_sum = 0
    for _ in range(101):
        start = time()
        part2(changes)
        times_sum += time() - start
    print(f'Mean over 100 runs: {(times_sum / 100) * 1000}ms')
