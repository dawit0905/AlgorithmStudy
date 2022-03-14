import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

left = 0
right = n-1
answer = sys.maxsize
answer_list = [0]*2
while left < right:
    total = arr[left]+arr[right]

    if abs(total) < answer:
        answer_list[0] = arr[left]
        answer_list[1] = arr[right]
        answer = abs(total)

    if total > 0:
        right -= 1
    elif total < 0:
        left += 1
    else:
        break

print(answer_list[0], answer_list[1])
