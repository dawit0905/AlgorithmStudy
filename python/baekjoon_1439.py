import sys


arr = list(map(int, list(sys.stdin.readline().rstrip())))

zero_set = 0
one_set = 0

count = 0
for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        count += 1


print((count+1)//2)