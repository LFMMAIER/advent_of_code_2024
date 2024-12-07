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

        #print(curx, cury)

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
