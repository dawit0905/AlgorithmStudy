import sys


arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

max_num = -1
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_num:
            max_num = arr[i][j]
            x = i+1
            y = j+1
print(max_num)
print(x, y)