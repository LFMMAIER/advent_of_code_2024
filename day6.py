def part1():
    total = 0

    arr = []

    curx, cury = 0, 0
    dir = 'N'

    y = 0
    f = open("day6/day6_input.txt", "r")
    for line in f:
        l = list(line.strip())

        if l.count('^') > 0:
            curx = l.index('^')
            cury = y

        y += 1
        arr.append(l)

    f.close()

    visited = set()

    while True:
        if (curx, cury) not in visited:
            total += 1
            visited.add((curx, cury))

        match dir:
            case 'N':
                if cury == 0:
                    break
                elif arr[cury - 1][curx] == "#":
                    dir = 'E'
                else:
                    cury -= 1

            case 'E':
                if curx == len(arr[0]) - 1:
                    break
                elif arr[cury][curx + 1] == "#":
                    dir = 'S'
                else:
                    curx += 1

            case 'S':
                if cury == len(arr) - 1:
                    break
                elif arr[cury + 1][curx] == "#":
                    dir = 'W'
                else:
                    cury += 1

            case 'W':
                if curx == 0:
                    break
                elif arr[cury][curx - 1] == "#":
                    dir = 'N'
                else:
                    curx -= 1

    print(total)


def part2():
    total = 0

    arr = []

    curx, cury = 0, 0
    dir = 'N'

    y = 0
    f = open("day6/day6_input.txt", "r")
    for line in f:
        l = list(line.strip())

        if l.count('^') > 0:
            curx = l.index('^')
            cury = y

        y += 1
        arr.append(l)

    f.close()

    orgx, orgy = curx, cury

    visited = set()

    while True:
        if (curx, cury) not in visited:
            visited.add((curx, cury))

        match dir:
            case 'N':
                if cury == 0:
                    break
                elif arr[cury - 1][curx] == "#":
                    dir = 'E'
                else:
                    cury -= 1

            case 'E':
                if curx == len(arr[0]) - 1:
                    break
                elif arr[cury][curx + 1] == "#":
                    dir = 'S'
                else:
                    curx += 1

            case 'S':
                if cury == len(arr) - 1:
                    break
                elif arr[cury + 1][curx] == "#":
                    dir = 'W'
                else:
                    cury += 1

            case 'W':
                if curx == 0:
                    break
                elif arr[cury][curx - 1] == "#":
                    dir = 'N'
                else:
                    curx -= 1


    lasty, lastx = None, None
    for item in visited:

        if lastx is not None:
            arr[lasty][lastx] = '.'
        
        curx, cury = orgx, orgy
        dir = 'N'
        v = set()

        arr[item[1]][item[0]] = '#'
        lasty, lastx = item[1], item[0]

        while True:
            if (curx, cury, dir) not in v:
                v.add((curx, cury, dir))
            else:
                total += 1
                break

            match dir:
                case 'N':
                    if cury == 0:
                        break
                    elif arr[cury - 1][curx] == "#":
                        dir = 'E'
                    else:
                        cury -= 1

                case 'E':
                    if curx == len(arr[0]) - 1:
                        break
                    elif arr[cury][curx + 1] == "#":
                        dir = 'S'
                    else:
                        curx += 1

                case 'S':
                    if cury == len(arr) - 1:
                        break
                    elif arr[cury + 1][curx] == "#":
                        dir = 'W'
                    else:
                        cury += 1

                case 'W':
                    if curx == 0:
                        break
                    elif arr[cury][curx - 1] == "#":
                        dir = 'N'
                    else:
                        curx -= 1
    

    print(total)


part1()
part2()