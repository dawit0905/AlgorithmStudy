import sys

sys.setrecursionlimit(10 ** 6)


def solution(x, y, n):
    color = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != arr[i][j]:
                solution(x, y, n // 3)
                solution(x, y + n // 3, n // 3)
                solution(x, y + (n // 3) * 2, n // 3)
                solution(x + n // 3, y, n // 3)
                solution(x + n // 3, y + n // 3, n // 3)
                solution(x + n // 3, y + (n // 3) * 2, n // 3)
                solution(x + (n // 3) * 2, y, n // 3)
                solution(x + (n // 3) * 2, y+n // 3, n // 3)
                solution(x + (n // 3) * 2, y + (n // 3) * 2, n // 3)
                return

    if color == -1:
        answer[0] += 1
    elif color == 0:
        answer[1] += 1
    else:
        answer[2] += 1


n = int(sys.stdin.readline())
arr = []
# -1, 0, 1
answer = [0, 0, 0]
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

solution(0, 0, n)
print(*answer)
