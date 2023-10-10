import sys


def dfs(a, b):
    if b == 1:
        return

    for i in range(a+int(1/3*b), a+int(2/3*b)):
        answer[i] = ' '
    dfs(a, b//3)
    dfs(a+b//3*2, b//3)


while True:
    try:
        n = int(sys.stdin.readline())
        answer = ['-'] * (3**n)
        dfs(0, 3**n)
        print(''.join(answer))
    except:
        break
