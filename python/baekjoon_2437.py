import sys


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
total = 1

for num in arr:
    if total < num:
        break

    total += num

print(total)
