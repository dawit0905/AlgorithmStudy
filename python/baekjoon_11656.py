import sys

_str = sys.stdin.readline().rstrip()
arr = []

for i in range(len(_str)):
    arr.append(_str[i:])

arr.sort()
print(*arr, sep="\n")