import re
from collections import namedtuple, defaultdict
from itertools import chain

claimRe = re.compile(r'#(\d+)\ @\ (\d+),(\d+):\ (\d+)x(\d+)')
Claim = namedtuple('Claim', ['number', 'x', 'y', 'width', 'height'])
Point = namedtuple('Point', ['x', 'y'])


def part1(claims):
    points = defaultdict(int)
    for claim in claims:
        for x in range(claim.x, claim.x + claim.width):
            for y in range(claim.y, claim.y + claim.height):
                points[Point(x, y)] += 1
    return len(list(filter(lambda a: a[1] >= 2, points.items())))


def part2(claims):
    point_claims = defaultdict(list)
    for claim in claims:
        for x in range(claim.x, claim.x + claim.width):
            for y in range(claim.y, claim.y + claim.height):
                point = Point(x, y)
                point_claims[point].append(claim)
    more_than_one_entry = set(
        chain(
            *map(
                lambda pc: pc[1],
                filter(lambda pc: len(pc[1]) > 1, point_claims.items())
            )
        )
    )
    return list((set(claims) - more_than_one_entry))[0].number


if __name__ == '__main__':
    claims = []
    with open('inputs/03') as f:
        claims = list(map(
            lambda l: Claim(*map(int, claimRe.match(l).groups())),
            filter(None, f.readlines())
        ))
    print(part1(claims))
    print(part2(claims))
