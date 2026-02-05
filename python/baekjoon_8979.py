import sys

N, K = map(int, sys.stdin.readline().split())
answer = 0
arr = []

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    arr.append(tmp)

arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))

index = 0
for i in range(N):
    if arr[i][0] == K:
        index = i
        break

for i in range(N):
    if arr[i][1:] == arr[index][1:]:
        answer = i + 1
        break

print(answer)
