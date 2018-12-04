from utils import nil
import re
import strutils
import strformat
import tables
import times
import sets
import hashes
import sequtils

type Claim = ref object of RootObj
    number*: int
    x*: int
    y*: int
    width*: int
    height*: int

proc `$`*(c: Claim): string =
    return &"#{c.number} @ {c.x},{c.y}: {c.width}x{c.height}"

proc hash*(c: Claim): Hash =
    var h: Hash = 0
    h = h !& hash(c.number)
    h = h !& hash(c.x)
    h = h !& hash(c.y)
    h = h !& hash(c.width)
    h = h !& hash(c.height)
    result = !$h

type Point = ref object of RootObj
    x*: int
    y*: int

proc `$`*(p: Point): string =
    return &"{p.x}x{p.y}"

proc part1(claims: seq[Claim]): int =
    var table = initCountTable[string](2)
    for claim in claims:
        for x in countup(claim.x, claim.x + claim.width - 1):
            for y in countup(claim.y, claim.y + claim.height - 1):
                table.inc(Point(x: x, y: y).`$`)
    for key, value in table.pairs:
        if value >= 2:
            result += 1

proc part2(claims: seq[Claim]): int =
    var table = initTable[string, seq[Claim]](2)
    for claim in claims:
        for x in countup(claim.x, claim.x + claim.width - 1):
            for y in countup(claim.y, claim.y + claim.height - 1):
                var point = Point(x: x, y: y).`$`
                if table.hasKey(point):
                    table[point].add(claim)
                else:
                    table[point] = @[claim]
    var more_than_one_entry = initSet[Claim]()
    for point, claims in table:
        if claims.len > 1:
            for claim in claims:
                more_than_one_entry.incl(claim)
    return claims.filter(proc (c: Claim): bool = not (c in more_than_one_entry))[0].number


when isMainModule:
    var lines = utils.readInputLines("03")
    var claims: seq[Claim] = @[]
    var reClaim = re"#(\d+)\ @\ (\d+),(\d+):\ (\d+)x(\d+)"
    for line in lines:
        var matches: array[5, string]
        discard match(line, reClaim, matches)
        claims.add(
            Claim(
                number: matches[0].parseInt,
                x: matches[1].parseInt,
                y: matches[2].parseInt,
                width: matches[3].parseInt,
                height: matches[4].parseInt
            )
        )
    echo part1(claims)
    echo part2(claims)
