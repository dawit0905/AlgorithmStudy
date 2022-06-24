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

s = [[] for _ in range(n+1)]
d = [0 for _ in range(n+1)]
temp = []
cnt = 0

for i in range(1, n+1):
    temp.append(list(map(int, sys.stdin.readline().split())))

print(temp)
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if temp[i][0] >= temp[j][0] and temp[i][1] >= temp[j][1] and temp[i][2] >= temp[j][2]:
            s[i].append(j)

print(s)
# for i in range(2):
#     for j in range(1, n+1):
#         visited = [0 for _ in range(n+1)]
#         if dfs(i):
#             cnt += 1
#
#
# print(s)
# print(cnt)