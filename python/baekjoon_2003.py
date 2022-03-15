import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left = 0
right = 1
cnt = 0

while right <= n and left <= right:
    total = sum(arr[left:right])

    if total == m:
        cnt += 1
        right += 1
    elif total < m:
        right += 1
    elif total > m:
        left += 1

print(cnt)
