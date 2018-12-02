from utils import nil
import tables
import sequtils
import strutils

proc part1(lines: seq[string]): int =
    var twoTotal = 0
    var threeTotal = 0
    for line in lines:
        var table = toCountTable(line)
        table.sort
        var two = false
        var three = false
        for pair in pairs(table):
            let count = pair[1]
            if count == 3:
                three = true
            elif count == 2:
                two = true
        if two:
            twoTotal += 1
        if three:
            threeTotal += 1
    return twoTotal * threeTotal

proc part2(lines: seq[string]): string =
    for target in lines:
        for line in lines:
            if target == line:
                continue
            var common: seq[char] = @[]
            for idx, alpha in line.pairs:
                if alpha == target[idx]:
                    common.add(alpha)
            if common.len == (line.len - 1):
                return common.join("")

when isMainModule:
    var lines = utils.readInputLines("02")
    echo part1(lines)
    echo part2(lines)
