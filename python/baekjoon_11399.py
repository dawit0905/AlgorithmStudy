import sys
n = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))
array_sum = [0 for i in range(n)]
array.sort()
for i in range(n):
    for j in range(0,i+1):
        array_sum[i] += array[j]

print(sum(array_sum))