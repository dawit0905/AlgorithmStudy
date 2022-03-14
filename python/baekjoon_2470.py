import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

_min = sys.maxsize
left = 0
right = n-1
answer = [0]*2

while left < right:
    total = arr[left] + arr[right]

    if abs(total) < _min:
        answer[0] = arr[left]
        answer[1] = arr[right]
        _min = abs(total)

    if total < 0:
        left += 1
    elif total > 0:
        right -= 1
    else:
        break

print(answer[0], answer[1])