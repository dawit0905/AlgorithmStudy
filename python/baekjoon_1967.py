import sys


def dfs(node, weight):

    for arr_node, arr_cost in array[node]:
        if distance[arr_node] == -1:
            distance[arr_node] = weight + arr_cost
            dfs(arr_node, weight+arr_cost)


sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())
array = [[] for _ in range(n+1)]
distance = [0]+[-1]*n
for i in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    array[a].append([b, c])
    array[b].append([a, c])

dfs(1, 0)

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))