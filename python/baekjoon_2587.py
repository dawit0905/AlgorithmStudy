import sys


arr = [int(sys.stdin.readline()) for i in range(5)]
arr.sort()

print(sum(arr) // 5)
print(arr[2])
