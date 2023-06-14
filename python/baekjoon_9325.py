import sys


t = int(sys.stdin.readline())

for tc in range(t):
    s = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    for i in range(n):
        q, p = map(int, sys.stdin.readline().split())
        s += q*p

    print(s)