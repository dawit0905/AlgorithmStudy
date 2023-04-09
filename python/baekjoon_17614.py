import sys


n = int(sys.stdin.readline())

answer = 0
for i in range(1, n+1):
    for s in str(i):
        if s == '3' or s == '6' or s == '9':
            answer += 1

print(answer)

