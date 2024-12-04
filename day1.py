def part1():
    total = 0

    left = []
    right = []

    f = open("day1/day1_input.txt", "r")
    for line in f:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    for i in range(len(left)):
        total += abs(left[i] - right[i])

    f.close()

    print(total)

import collections

def part2():
    total = 0

    left = []
    right = []

    f = open("day1/day1_input.txt", "r")
    for line in f:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    l = collections.Counter(left)
    r = collections.Counter(right)

    for key in l.keys():
        if key in r:
            total += key * l[key] * r[key]

    f.close()

    print(total)


part1()
part2()
