import re

def part1():
    total = 0

    f = open("day3/day3_input.txt", "r")
    for line in f:
        search = r"mul\(\d+,\d+\)"
        ret = re.findall(search, line)

        for item in ret:
            x, y = item.split(",")
            total += int(x[4:]) * int(y[:-1])

    f.close()

    print(total)


def part2():
    total = 0

    enable = True

    f = open("day3/day3_input.txt", "r")
    for line in f:
        search = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
        
        ret = re.findall(search, line)

        for item in ret:
            if item == "do()":
                enable = True
            elif item == "don't()":
                enable = False
            else:
                if enable:
                    x, y = item.split(",")
                    total += int(x[4:]) * int(y[:-1])

    f.close()

    print(total)


part1()
part2()
