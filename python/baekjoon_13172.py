import sys
from math import gcd


def mul(x, y):
    if y == 1:
        return x
    if y % 2 == 1:
        return x * mul(x, y-1) % mod
    left = mul(x, y // 2)
    return left * left % mod


m = int(sys.stdin.readline())
answer = 0
mod = int(1e9+7)
for _ in range(m):
    n, s = map(int, sys.stdin.readline().split())
    g = gcd(n, s)

    n //= g
    s //= g

    answer += s * mul(n, mod-2) % mod
    answer %= mod

print(answer)


