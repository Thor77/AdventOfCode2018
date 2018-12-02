from utils import nil
import strutils
import sequtils
import strformat
import times
import math
import sets

proc part1(changes: seq[int]): int =
    return changes.sum

proc part2(changes: seq[int]): int =
    var seen = initSet[int]()
    while true:
        for change in changes:
            result += change
            if seen.contains(result):
                return result
            seen.incl(result)

when isMainModule:
    var input = utils.readInputLines("01").map(parseInt)
    echo part1(input)
    assert part2(@[+3, +3, +4, -2, -4]) == 10
    assert part2(@[+1, -1]) == 0
    assert part2(@[-6, +3, +8, +5, -6]) == 5
    assert part2(@[+7, +7, -2, -7, -4]) == 14
    var sumTime: float
    var startTime: float
    for _ in 0..101:
        startTime = epochTime()
        discard part2(input)
        sumTime += (epochTime() - startTime)
    echo &"Mean over 100 runs: {(sumTime / 100) * 1000}ms"
