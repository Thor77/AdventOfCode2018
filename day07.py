import re
from collections import defaultdict, namedtuple
from operator import attrgetter


lineRe = re.compile(r'Step (\w) must be finished before step (\w) can begin')
Step = namedtuple('Step', ['prereq', 'name'])


def part1(steps):
    name_prereqs = defaultdict(set)
    for step in steps:
        name_prereqs[step.name].add(step.prereq)
    all_names = set(map(attrgetter('name'), steps))
    all_prereqs = set(map(attrgetter('prereq'), steps))
    all_steps = all_names.copy()
    all_steps.update(all_prereqs)
    # find step without preqreqs
    no_prereqs = all_prereqs - all_names
    for no_prereq in no_prereqs:
        name_prereqs[no_prereq] = set()
    order = []
    while True:
        available_steps = [
            name
            for name, prereqs in name_prereqs.items()
            if not list(filter(lambda p: p not in order, prereqs))
        ]
        available_steps = sorted(available_steps)
        if not available_steps:
            break
        next_step = available_steps[0]
        del name_prereqs[next_step]
        order.append(next_step)
    return ''.join(order)


if __name__ == '__main__':
    steps = []
    with open('inputs/07') as f:
        steps = [
            Step(*lineRe.match(line).groups())
            for line in f
        ]
    print(part1(steps))
