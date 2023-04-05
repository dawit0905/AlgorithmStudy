import sys


a, b = sys.stdin.readline().strip().split()

if len(a) < len(b):
    gap = len(b)-len(a)
    result = sys.maxsize
    for i in range(gap+1):
        temp = 0
        for j in range(len(a)):
            if b[j+i] != a[j]:
                temp += 1

        result = min(result, temp)

    print(result)

else:
    result = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            result += 1

    print(result)
