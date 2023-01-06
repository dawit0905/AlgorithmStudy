import sys


def gcd(a, b):
    if a%b == 0:
        return b

    return gcd(b, a%b)


tc = int(sys.stdin.readline())

for t in range(tc):
    n, *arr = list(map(int, sys.stdin.readline().split()))
    answer = 0
    for i in range(n):
        for j in range(i+1, n):
            answer += gcd(arr[i], arr[j])
    print(answer)
