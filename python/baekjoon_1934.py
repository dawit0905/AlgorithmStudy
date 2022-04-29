import sys


def gcd(b, a):
    if a == 0:
        return b

    return gcd(a, b%a)

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a*b//gcd(b, a))

