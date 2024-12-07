def part1():
    total = 0

    rules = {}

    space = True
    f = open("day5/day5_input.txt", "r")
    for line in f:
        if len(line) == 1:
            space = False
            continue

        if space:
            x, y = line.split("|")
            if int(y) in rules:
                temp = rules[int(y)]
                temp.add(int(x))
                rules[int(y)] = temp
            else:
                temp = set()
                temp.add(int(x))
                rules[int(y)] = temp

        else:
            arr = [int(x) for x in line.split(",")]
            
            valid = True

            seen = set()
            for item in arr[::-1]:
                seen.add(item)
                if item not in rules:
                    continue
                elif len(seen.intersection(rules[item])) > 0:
                    valid = False
                    break

            if valid:
                mid = arr[len(arr) // 2]
                total += mid

    f.close()

    print(total)

from functools import cmp_to_key

def part2():
    total = 0

    rules = {}

    def order(a, b):
        if a not in rules:
            return 1
        elif b not in rules:
            return -1

        if a in rules[b]:
            return 1
        elif b in rules[a]:
            return -1
        else:
            return 0


    space = True
    f = open("day5/day5_input.txt", "r")
    for line in f:
        if len(line) == 1:
            space = False
            continue

        if space:
            x, y = line.split("|")
            if int(y) in rules:
                temp = rules[int(y)]
                temp.add(int(x))
                rules[int(y)] = temp
            else:
                temp = set()
                temp.add(int(x))
                rules[int(y)] = temp

        else:
            arr = [int(x) for x in line.split(",")]
            
            valid = True

            seen = set()
            for item in arr[::-1]:
                seen.add(item)
                if item not in rules:
                    continue
                elif len(seen.intersection(rules[item])) > 0:
                    valid = False
                    break

            if not valid:
                arr.sort(key=cmp_to_key(order))
                mid = arr[len(arr) // 2]
                total += mid

    print(total)



part1()
part2()
