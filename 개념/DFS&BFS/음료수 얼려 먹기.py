import sys

def dfs(x,y):
    if x <= -1 or x >= n or y<= -1 or y>= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
n,m = map(int,sys.stdin.readline().split())
graph = []
count = 0
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1

print(count)