import sys


def gcd(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp

    return a


def lcm(a, b):
    return a * b // gcd(a, b)


n = int(sys.stdin.readline())

arr = []
for i in list(map(int, sys.stdin.readline().split())):
    arr.append([1, i])

a = arr[0][0]
b = arr[0][1]

for i in range(1, n):
    lcmv = lcm(arr[i][1], b)
    arr[i][0] = lcmv // arr[i][1] * arr[i][0]
    a = lcmv // b * a + arr[i][0]
    b = lcmv

gcdv = gcd(a, b)

print(f'{b//gcdv}/{a//gcdv}')
