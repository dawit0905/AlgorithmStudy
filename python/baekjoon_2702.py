import sys


def gcd(a, b):

    if a == 0:
        return b

    return gcd(b % a, a)


tc = int(sys.stdin.readline())

for t in range(tc):
    a, b = map(int, sys.stdin.readline().split())
    num = gcd(a, b)
    print(a*b // num, num)