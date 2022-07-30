import sys

n = int(sys.stdin.readline())
cnt = 0
for i in range(n):
    answer = int(sys.stdin.readline())
    if answer == 1:
        cnt += 1

if cnt > (n // 2):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')