import sys


idx = 1
while True:

    l, p, v = map(int ,sys.stdin.readline().split())
    if l == 0 and p == 0 and v == 0:
        break

    result = v // p * l

    remainder = v % p
    if remainder > l:
        result += l
    else:
        result += remainder

    print(f'Case {idx}: {result}')
    idx += 1

