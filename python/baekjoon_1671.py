import sys


def dfs(start):
    if visited[start] == 1:
        return 0
    visited[start] = 1

    for i in s[start]:
        if d[i] == 0 or dfs(d[i]):
            d[i] = start
            return 1
    return 0


n = int(sys.stdin.readline())
# 기본적으로 d의 0이 선택받지 못한 노드로 생각되기 때문에,
# 1, n+1 범위의 값을 사용하고, 마지막에 0의 개수를 출력하면 된다.
s = [[0] * (n+1) for _ in range(n+1)]
d = [0 for _ in range(n+1)]
# temp = [[]] i, j 값이 1개 높기 때문에 넣어줘야됨.
temp = [[]]

for i in range(n):
    temp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        if temp[i][0] == temp[j][0] and temp[i][1] == temp[j][1] and temp[i][2] == temp[j][2] and i > j:
            continue
        if temp[i][0] >= temp[j][0] and temp[i][1] >= temp[j][1] and temp[i][2] >= temp[j][2]:
            s[i].append(j)


for i in range(2):
    for j in range(1, n+1):
        visited = [0 for _ in range(n+1)]
        dfs(j)


print(d.count(0))
