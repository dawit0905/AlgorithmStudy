import sys

tc = int(sys.stdin.readline())

for t in range(tc):
    n = int(sys.stdin.readline().rstrip())
    s = bin(n)[2:]
    cnt = 0
    for i in s[::-1]:
        if i == '1':
            print(cnt, end=" ")
        cnt += 1