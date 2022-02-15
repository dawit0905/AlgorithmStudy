import sys
from collections import deque

def bfs(start):

    que = deque()
    cnt = 0
    for i in edge_data[start]:
        que.append(i)
        visited[i] = 1
        cnt += 1

    while que:
        node = que.popleft()
        for i in edge_data[node]:
            if visited[i] != 1:
                que.append(i)
                visited[i] = 1
                cnt+=1
    return cnt

node_cnt = int(sys.stdin.readline())
edge_cnt = int(sys.stdin.readline())
edge_data = [[] for i in range(node_cnt+1)]
visited = [0,1] + [ 0 for i in range(node_cnt-1)]

for i in range(edge_cnt):
    a,b = map(int, sys.stdin.readline().split())
    edge_data[a].append(b)
    edge_data[b].append(a)

print(bfs(1))
# print(visited)
