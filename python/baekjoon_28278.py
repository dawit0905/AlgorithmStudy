import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    operator = list(map(int, sys.stdin.readline().split()))

    if operator[0] == 1:
        stack.append(operator[1])
    elif operator[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif operator[0] == 3:
        print(len(stack))
    elif operator[0] == 4:
        print(1) if not stack else print(0)
    else:
        print(stack[-1]) if stack else print(-1)


