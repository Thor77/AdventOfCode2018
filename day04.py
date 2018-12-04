import re
from collections import namedtuple, defaultdict
from datetime import datetime

from operator import attrgetter

actionRe = re.compile(r'\[(\d\d\d\d-\d\d-\d\d\ \d\d:\d\d)\]\ (.*)')
Action = namedtuple('Action', ['timestamp', 'action'])
Guard = namedtuple('Guard', ['name', 'minutes_asleep', 'minutes'])


def build_guards(actions):
    guards = {}
    current_guard_name = None
    current_sleep_start = None
    for action in actions:
        if 'begins shift' in action.action:
            current_guard_name = int(action.action.split()[1].lstrip('#'))
            guards.setdefault(
                current_guard_name,
                Guard(current_guard_name, 0, defaultdict(int))
            )
        elif action.action == 'falls asleep':
            current_sleep_start = action.timestamp
        elif action.action == 'wakes up':
            sleep_time = action.timestamp - current_sleep_start
            guard = guards[current_guard_name]
            for i in range(current_sleep_start.minute, action.timestamp.minute):
                guard.minutes[i] += 1
            new_minutes_asleep = guard.minutes_asleep + \
                int(sleep_time.total_seconds() / 60)
            guards[current_guard_name] = guard._replace(
                minutes_asleep=new_minutes_asleep
            )
    return guards


def part1(actions):
    guards = build_guards(actions)
    most_sleeping_guard = sorted(
        guards.items(), key=lambda kv: kv[1].minutes_asleep, reverse=True
    )[0][1]
    most_sleeping_minute = sorted(
        most_sleeping_guard.minutes.items(), key=lambda kv: kv[1], reverse=True
    )[0][0]
    return most_sleeping_guard.name * most_sleeping_minute


def part2(actions):
    def most_slept_minute(guard):
        if not guard.minutes:
            return (0, 0)
        return sorted(
            guard.minutes.items(), key=lambda kv: kv[1], reverse=True
        )[0]

    guards = build_guards(actions)
    guards_msm = map(
        lambda kv: (*kv, most_slept_minute(kv[1])), guards.items()
    )
    name, guard, msm = sorted(guards_msm, key=lambda g: g[2][1], reverse=True)[0]
    return guard.name * msm[0]


if __name__ == '__main__':
    actions = []
    with open('inputs/04') as f:
        actions = list(map(
            lambda l: Action(
                datetime.strptime(l.group(1), '%Y-%m-%d %H:%M'), l.group(2)
            ),
            map(actionRe.match, filter(None, f.readlines()))
        ))
    actions = list(sorted(actions, key=attrgetter('timestamp')))
    print(part1(actions))
    print(part2(actions))
