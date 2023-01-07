import sys


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a%b)


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
g = gcd(arr[0], gcd(arr[1], arr[-1]))

for i in range(1, g//2+1):
    if g % i == 0:
        print(i)

print(g)
