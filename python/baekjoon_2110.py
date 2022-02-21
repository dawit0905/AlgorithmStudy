import sys

n, c = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

left = 1
right = arr[n-1] - arr[0]
d = 0
ans = 0

while left <= right:
    mid = (left+right) // 2
    start = arr[0]
    cnt = 1

    for i in range(1, n):
        d = arr[i] - start
        if mid <= d:
            cnt += 1
            start = arr[i]

    # 공유기의 수를 줄이자, 간격 넓히기
    if cnt >= c:
        ans = mid
        left = mid + 1
    # 공유기가 더 설치되어야 된다. 간격 좁히기
    else :
        right = mid - 1

print(ans)