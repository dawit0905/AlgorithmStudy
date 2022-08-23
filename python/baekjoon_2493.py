import sys


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
answer = []

for i in range(n):
    while stack:
        if arr[stack[-1]] >= arr[i]:
            break
        else:
            stack.pop()
    if stack:
        answer.append(stack[-1] + 1)
    else:
        answer.append(0)
    stack.append(i)
print(*answer)
