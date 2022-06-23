import sys

n, m = map(int, sys.stdin.readline().split())
a = [i**2 for i in range(2, int(m**0.5)+1)]
num = [1] * (m-n+1)

for i in a:
    number = n//i*i
    while(number <= m):
        if number - n >= 0:
            num[number-n] = 0
        number += i
print(sum(num))
