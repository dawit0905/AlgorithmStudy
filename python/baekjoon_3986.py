import sys


n = int(sys.stdin.readline())
cnt = 0

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    stack = []

    for i in range(len(s)):
        if stack:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    if not stack:
        cnt += 1

print(cnt)
