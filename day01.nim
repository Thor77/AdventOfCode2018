from utils import nil
import strutils
import sequtils
import math

proc part1(changes: seq[int]): int =
    return changes.sum

proc part2(changes: seq[int]): int =
    var seen = @[0]
    while true:
        for change in changes:
            result += change
            if result in seen:
                return result
            seen.add(result)

when isMainModule:
    var input = utils.readInputLines("01").map(parseInt)
    echo part1(input)
    assert part2(@[+3, +3, +4, -2, -4]) == 10
    assert part2(@[+1, -1]) == 0
    assert part2(@[-6, +3, +8, +5, -6]) == 5
    assert part2(@[+7, +7, -2, -7, -4]) == 14
    echo part2(input)
