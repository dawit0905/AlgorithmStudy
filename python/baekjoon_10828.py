import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    str = sys.stdin.readline().rstrip()
    if 'push' in str:
        num = int(str.split()[1])
        stack.append(num)
    elif 'top' in str:
        if len(stack) != 0:
            print(stack[-1])
        else :
            print(-1)
    elif 'size' in str:
        print(len(stack))
    elif 'empty' in str:
        if len(stack) >= 1 :
            print(0)
        else :
            print(1)
    elif 'pop' in str:
        if len(stack) == 0:
            print(-1)
        else :
            print(stack.pop())