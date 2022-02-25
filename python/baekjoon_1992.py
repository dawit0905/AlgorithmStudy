import sys

'''
input
8
00000000
00000000
00001111
00001111
00011111
00111111
00111111
00111111

output
(0(0011)(0(0111)01)1)
'''


def solution(x, y, n):
    color = data[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != data[i][j]:
                print('(', end='')
                solution(x, y, n // 2)
                solution(x, y + n // 2, n // 2)
                solution(x + n // 2, y, n // 2)
                solution(x + n // 2, y + n // 2, n // 2)
                print(')', end='')
                return
    if color == 0:
        print('0', end='')
    else:
        print('1', end='')


n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().rstrip())) for i in range(n)]
solution(0, 0, n)
