import sys


def dfs(x):
    global cnt
    # 자식노드가 없다면 cnt+=1
    if x not in arr and x != del_node:
        cnt += 1
        return
    # 자식노드가 있다면 그 자식노드들을 dfs로 탐색한다.
    else:
        for i in range(n):
            if arr[i] == x and i != del_node:
                dfs(i)
        return cnt


sys.setrecursionlimit(10000)
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
del_node = int(sys.stdin.readline())
start = arr.index(-1)
cnt = 0

if start == del_node:
    print(cnt)
else:
    dfs(start)
    if arr.count(arr[del_node]) == 1:
        cnt += 1
    print(cnt)
