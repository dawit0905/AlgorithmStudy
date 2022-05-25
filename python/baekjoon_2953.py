import sys

total = 0
index = 0
for i in range(5):
    arr = list(map(int, sys.stdin.readline().split()))
    if total < sum(arr):
        total = sum(arr)
        index = i+1

print(index, total)