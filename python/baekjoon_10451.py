import sys


def dfs(now, temp_list):
    global cnt

    if now in temp_list:
        cnt += 1
        return

    visited[now] = 1
    temp_list.append(now)
    temp_list.append(now)
    dfs(arr[now], temp_list)


test_case = int(sys.stdin.readline())
sys.setrecursionlimit(int(10e7))
for tc in range(test_case):
    n = int(sys.stdin.readline())
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0] * (n+1)
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i, [])

    print(cnt)