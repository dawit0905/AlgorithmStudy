import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
arr2 = []

arr = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))
answer = []

arr_index = 0
arr2_index = 0
for i in range(n+m):
    if arr_index == n:
        answer.append(arr2[arr2_index])
        arr2_index += 1
        continue
    elif arr2_index == m:
        answer.append(arr[arr_index])
        arr_index += 1
        continue

    if arr[arr_index] <= arr2[arr2_index]:
        answer.append(arr[arr_index])
        arr_index += 1
    else:
        answer.append(arr2[arr2_index])
        arr2_index += 1

print(*answer)