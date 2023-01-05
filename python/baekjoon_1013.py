import sys
import re


tc = int(sys.stdin.readline())

for t in range(tc):
    s = sys.stdin.readline().rstrip()
    pattern = re.compile('(100+1+|01)+')
    model = pattern.fullmatch(s)
    if model:
        print('YES')
    else:
        print('NO')
