import sys

n = int(sys.stdin.readline())

for i in range(n):
    n,m = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))

    check = [0 for _ in range(n)]
    check[m] = 1
    count = 1

    while array:
        if array[0] == max(array):
            if check[0] == 1:
                print(count)
                break
            else :
                array.pop(0)
                check.pop(0)
                count += 1
        else :
            array.append(array.pop(0))
            check.append(check.pop(0))