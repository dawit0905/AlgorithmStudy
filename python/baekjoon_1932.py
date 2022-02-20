import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            arr[i][j] += arr[i-1][j]
            continue
        elif i == j:
            arr[i][j] += arr[i - 1][j-1]
            continue
        else :
            arr[i][j] += max(arr[i-1][j],arr[i - 1][j-1])
print(max(arr[-1]))