import sys


n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.append(arr[0])

sum1 = 0
for i in range(0, len(arr)-1):
    sum1 += arr[i][0] * arr[i+1][1]

sum2 = 0
for i in range(0, len(arr)-1):
    sum2 += arr[i][1] * arr[i+1][0]

print(abs(round((sum1-sum2)/2, 1)))