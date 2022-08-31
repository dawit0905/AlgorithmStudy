import sys


n, m = map(int, sys.stdin.readline().split())
_set = set()
cnt = 0

for i in range(n):
    _str = sys.stdin.readline().rstrip()
    _set.add(_str)

for i in range(m):
    _str = sys.stdin.readline().rstrip()
    if _str in _set:
        cnt += 1

print(cnt)
