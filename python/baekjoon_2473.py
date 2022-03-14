import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
temp = sys.maxsize
answer = [0]*3

for i in range(n-2):
    left = i+1
    right = n-1
    while left < right:
        total = arr[i]+arr[left]+arr[right]

        if abs(total) < abs(temp):
            answer[0] = arr[i]
            answer[1] = arr[left]
            answer[2] = arr[right]
            temp = total

        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else:
            print(*answer)
            sys.exit(0)
print(*answer)
