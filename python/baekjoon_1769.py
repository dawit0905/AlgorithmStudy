import sys


def recur(s, cnt):
    if len(s) > 1:
        total = 0
        for i in s:
            total += int(i)
        return recur(str(total), cnt + 1)
    else:
        if int(s) % 3 == 0:
            print(cnt)
            print('YES')
        else:
            print(cnt)
            print('NO')


x = sys.stdin.readline().rstrip()
recur(x, 0)
