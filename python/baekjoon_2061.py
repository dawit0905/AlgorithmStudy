import sys


k, l = map(int, sys.stdin.readline().split())

for i in range(2, l):
    if k % i == 0:
        if i < l:
            print(f'BAD {i}')
            exit(0)
print('GOOD')
