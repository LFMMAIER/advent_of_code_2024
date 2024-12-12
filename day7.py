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

part1()
