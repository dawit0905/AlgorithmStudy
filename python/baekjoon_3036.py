import sys


def gcd(a, b):
    if a%b == 0:
        return b

    if b == 0:
        return a

    return gcd(b, a%b)


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    ans = gcd(arr[0], arr[i])
    print(f'{arr[0]//ans}/{arr[i]//ans}')
