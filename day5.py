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


part1()
#part2()
