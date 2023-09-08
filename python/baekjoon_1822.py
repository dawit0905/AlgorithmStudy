import sys


a, b = map(int, sys.stdin.readline().split())
A = set(list(map(int, sys.stdin.readline().split())))
B = set(list(map(int, sys.stdin.readline().split())))

result = list(A-B)
if result:
    result = sorted(list(result))
    print(len(result))
    print(*result)
else:
    print(0)


