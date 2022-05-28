import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

visited = [0 for _ in range(101)]
result = 0
for i in arr:
    if visited[i] != 0:
        result += 1
    else:
        visited[i] += 1

print(result)