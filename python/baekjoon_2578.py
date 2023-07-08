import sys


def check(arr):
    cnt = 0
    # 가로
    for i in range(5):
        for j in range(5):
            if arr[i][j] != 1:
                break
        else:
            cnt += 1
    # 세로
    for i in range(5):
        for j in range(5):
            if arr[j][i] != 1:
                break
        else:
            cnt += 1
    # 왼쪽-대각선
    for i in range(5):
        if arr[i][i] != 1:
            break
    else:
        cnt += 1
    # 오른쪽-대각선
    for i in range(5):
        if arr[i][4-i] != 1:
            break
    else:
        cnt += 1

    return cnt


graph = []
for i in range(5):
    graph.append(list(map(int, sys.stdin.readline().split())))

numbers = []
for i in range(5):
    numbers.extend(list(map(int, sys.stdin.readline().split())))

visited = [[0] * 5 for _ in range(5)]
for num in range(len(numbers)):
    for i in range(5):
        for j in range(5):
            if graph[i][j] == numbers[num]:
                visited[i][j] = 1

    if check(visited) >= 3:
        print(num+1)
        break