import sys


n = int(sys.stdin.readline())
grundy = 0
arr = list(map(int, sys.stdin.readline().split()))

for i in arr:
    grundy ^= i

if grundy:
    print('koosaga')
else:
    print("cubelover")