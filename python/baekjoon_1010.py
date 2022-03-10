import sys
from math import factorial
T = int(sys.stdin.readline())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    answer = factorial(m) // (factorial(n) * factorial(m-n))
    print(answer)
