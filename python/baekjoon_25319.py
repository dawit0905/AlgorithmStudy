import sys


n, m, s = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))
id = sys.stdin.readline().rstrip()
dictionary = {}
xy_map = {}
for i in id:
    dictionary[i] = 0
    xy_map[i] = []


for i in range(n):
    for j in range(m):
        word = graph[i][j]
        if word in dictionary:
            dictionary[word] += 1
            xy_map[word].append((i,j))

cnt = sys.maxsize
for key, value in list(dictionary.items()):
    appear_num = id.count(key)
    cnt = min(cnt, value//appear_num)
C = cnt

answer = ''
visited = [[0] * m for _ in range(n)]
id = id*cnt
x, y = 0, 0

for word in id:
    point_x, point_y = xy_map[word].pop(0)

    if x < point_x:
        answer += 'D'*(point_x - x)
    if x > point_x:
        answer += 'U'*abs((point_x - x))
    if y < point_y:
        answer += 'R'*(point_y - y)
    if y > point_y:
        answer += 'L'*abs((point_y - y))

    answer += 'P'
    x, y = point_x, point_y


answer += 'D'*((n-1)-x)
answer += 'R'*((m-1)-y)

print(C, len(answer))
print(answer)
