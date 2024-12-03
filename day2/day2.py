def part1():
    total = 1000

    f = open("day2_input.txt", "r")
    for line in f:
        arr = line.split()

        asc = int(arr[0]) > int(arr[1])

        for i in range(len(arr) - 1):
            jmp = int(arr[i]) - int(arr[i + 1])
            if asc and (jmp > 3 or jmp < 1):
                total -= 1
                break
            elif not asc and (jmp < -3 or jmp > -1):
                total -= 1
                break

    f.close()

    print(total)


def part2():
    total = 0

    def check(a):
        asc = a[0] > a[1]

        for i in range(len(a) - 1):
            jmp = a[i] - a[i + 1]
                
            if asc and (jmp > 3 or jmp < 1):
                return 0
            elif not asc and (jmp < -3 or jmp > -1):
                return 0
        
        return 1

    f = open("day2_input.txt", "r")
    for line in f:
        arr = [int(x) for x in line.split()]

        if check(arr):
            total += 1
        else:
            for i in range(len(arr)):
                narr = arr[:]
                narr.pop(i)
                if check(narr):
                    total += 1
                    break

    f.close()

    print(total)


part1()
part2()
