import sys

answer = 0
while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break

    answer += n

print(answer)