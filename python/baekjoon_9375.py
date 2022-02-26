import sys
from collections import Counter

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    s = []
    for j in range(n):
        costume_name, costume = map(str, sys.stdin.readline().rstrip().split())
        s.append(costume)
    num = 1
    result = Counter(s)
    for key in result:
        num *= result[key] + 1
    print(num - 1)
