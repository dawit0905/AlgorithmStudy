import sys


n = int(sys.stdin.readline())
_set = set()
for i in range(n):
    a, b = map(str, sys.stdin.readline().rstrip().split())

    if b == 'enter':
        _set.add(a)
    elif b == 'leave':
        _set.remove(a)

arr = list(_set)
arr.sort(reverse=True)

for i in arr:
    print(i)
