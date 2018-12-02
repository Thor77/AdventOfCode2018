from utils import nil
import tables
import sequtils

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

when isMainModule:
    var lines = utils.readInputLines("02")
    echo part1(lines)
