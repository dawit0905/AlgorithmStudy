import sys


n, t = map(int, sys.stdin.readline().split())
start_time = []
answer = 0
for i in range(n):
    s, i, c = map(int, sys.stdin.readline().split())

    idx = 0
    num = s
    while idx < c:
        start_time.append(num)
        num += i
        idx += 1

result = []
start = 0
end = len(start_time) - 1

while start <= end:
    mid = (start+end) // 2


    if start_time[mid] >= t:
        answer = mid
        end = mid - 1
    elif start_time[mid] > t:
        start = mid + 1

    result.append(start_time[answer] - t)


if result:
    print(min(result))
else:
    print(-1)