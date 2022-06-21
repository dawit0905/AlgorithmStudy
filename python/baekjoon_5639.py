import sys


def dfs(start, end):
    if start > end:
        return

    mid = end + 1

    # 오른쪽 자식노드를 찾는중..
    for i in range(start + 1, end + 1):
        if tree[start] < tree[i]:
            mid = i
            break

    dfs(start + 1, mid - 1)
    dfs(mid, end)
    print(tree[start])


sys.setrecursionlimit(10**9)
tree = []
for i in range(10000):
    try:
        num = int(sys.stdin.readline())
        tree.append(num)
    except:
        break

dfs(0, len(tree) - 1)
