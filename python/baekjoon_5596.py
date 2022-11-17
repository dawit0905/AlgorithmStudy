import sys


arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))


print(max(sum(arr1), sum(arr2)))

