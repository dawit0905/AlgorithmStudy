import sys


n = sys.stdin.readline().rstrip()
f = int(sys.stdin.readline())

answer = int(n[:-2] + '00')

while True:
    if answer % f == 0:
        break
    answer += 1

print(str(answer)[-2:])
