import sys


def dfs(node, weight):
    for arr_node, arr_cost in array[node]:
        if distance[arr_node] == -1:
            distance[arr_node] = weight + arr_cost
            dfs(arr_node, weight+arr_cost)


n = int(sys.stdin.readline())
array = [[] for _ in range(n+1)]
distance = [0]+[-1]*n

for i in range(1, n+1):
    temp = list(map(int, sys.stdin.readline().split()))
    index = temp.pop(0)
    temp.pop(-1)
    for j in range(0, len(temp), 2):
        array[index].append([temp[j], temp[j+1]])


dfs(1, 0)

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))