import sys


t = int(sys.stdin.readline())

for tc in range(t):
    v, e = map(int, sys.stdin.readline().split())

    for i in range(1, 100):
        if v - e + i == 2:
            print(i)
            break