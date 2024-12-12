def part1():
    total = 0

    f = open("day7/day7_input.txt", "r")
    for line in f:
        
        arr = [int(x) for x in line.split(":")[1].strip().split()]

        s = int(line.split(":")[0])
    
        size = len(arr) - 1
        for i in range(2 ** size):
            combo = list(f'{i:0{size}b}')
            
            cur = arr[0]

            for j, item in enumerate(combo):
                if item == '0':
                    cur *= arr[j + 1]
                else:
                    cur += arr[j + 1]

            if cur == s:
                total += s
                break


    f.close()

    print(total)


def part2():
    total = 0


    def ternary(n):
        r = n // 3
        q = n % 3
        if n == 0:
            return '0'
        
        elif r == 0:
            return str(q)
        
        else:
            return ternary(r) + str(q)


    f = open("day7/day7_input.txt", "r")
    for line in f:
        
        arr = [int(x) for x in line.split(":")[1].strip().split()]

        s = int(line.split(":")[0])
    
        size = len(arr) - 1
        for i in range(3 ** size):
            combo = list(f'{ternary(i)[::-1]:0{size}}')
            
            cur = arr[0]

            for j, item in enumerate(combo):
                if item == '0':
                    cur *= arr[j + 1]
                elif item == '1':
                    cur += arr[j + 1]
                else:
                    cur = int(str(cur) + str(arr[j + 1]))

            if cur == s:
                total += s
                break


    f.close()

    print(total)


part1()
part2()
