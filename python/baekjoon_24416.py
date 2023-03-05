import sys


def fib(n):
    if n == 1 or n == 2:
        return 1

    return fib(n-1) + fib(n-2)


def fibonacci(n):
    f = [0, 1, 1] + [0] * (n)
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]

    # print(f)
    return f[n]


n = int(sys.stdin.readline())
print(fibonacci(n), n-2)
