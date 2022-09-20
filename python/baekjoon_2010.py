import sys


n = int(sys.stdin.readline())
result = 0
for i in range(n):
    result += int(sys.stdin.readline())

print(result-n+1)
