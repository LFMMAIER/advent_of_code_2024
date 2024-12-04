def part1():
    total = 0

    arr = []

    f = open("day4/day4_input.txt", "r")
    for line in f:
        arr.append(list(line))

    for j in range(len(arr)):
        for i in range(len(arr[0])):

            # horizontal
            if (i + 3 < len(arr[0])):
                if arr[j][i] == 'X' and arr[j][i + 1] == 'M' and arr[j][i + 2] == 'A' and arr[j][i + 3] == 'S':
                    total += 1
                elif arr[j][i] == 'S' and arr[j][i + 1] == 'A' and arr[j][i + 2] == 'M' and arr[j][i + 3] == 'X':
                    total += 1

            # vertical
            if (j + 3 < len(arr)):
                if arr[j][i] == 'X' and arr[j + 1][i] == 'M' and arr[j + 2][i] == 'A' and arr[j + 3][i] == 'S':
                    total += 1
                elif arr[j][i] == 'S' and arr[j + 1][i] == 'A' and arr[j + 2][i] == 'M' and arr[j + 3][i] == 'X':
                    total += 1

            # diagonal right
            if (j + 3 < len(arr) and i + 3 < len(arr[0])):
                if arr[j][i] == 'X' and arr[j + 1][i + 1] == 'M' and arr[j + 2][i + 2] == 'A' and arr[j + 3][i + 3] == 'S':
                    total += 1
                elif arr[j][i] == 'S' and arr[j + 1][i + 1] == 'A' and arr[j + 2][i + 2] == 'M' and arr[j + 3][i + 3] == 'X':
                    total += 1

            # diagonal left
            if (j + 3 < len(arr) and i > 2):
                if arr[j][i] == 'X' and arr[j + 1][i - 1] == 'M' and arr[j + 2][i - 2] == 'A' and arr[j + 3][i - 3] == 'S':
                    total += 1
                elif arr[j][i] == 'S' and arr[j + 1][i - 1] == 'A' and arr[j + 2][i - 2] == 'M' and arr[j + 3][i - 3] == 'X':
                    total += 1

    f.close()

    print(total)

def part2():
    total = 0

    arr = []

    f = open("day4/day4_input.txt", "r")
    for line in f:
        arr.append(list(line))

    allowed = set()
    allowed.add('M')
    allowed.add('S')

    for j in range(len(arr)):
        for i in range(len(arr[0]) - 1):

            if arr[j][i] == 'A'and (i + 1 < len(arr[0]) - 1 and i > 0 and j + 1 < len(arr) and j > 0):
                c = []
                
                if arr[j - 1][i - 1] in allowed:
                    c.append(arr[j - 1][i - 1])
                else:
                    continue

                if arr[j + 1][i + 1] in allowed:
                    c.append(arr[j + 1][i + 1])
                else:
                    continue

                if arr[j + 1][i - 1] in allowed:
                    c.append(arr[j + 1][i - 1])
                else:
                    continue

                if arr[j - 1][i + 1] in allowed:
                    c.append(arr[j - 1][i + 1])
                else:
                    continue
                
                if c.count('M') == 2 and c[0] != c[1]:
                    total += 1

    f.close()

    print(total)

part1()
part2()
