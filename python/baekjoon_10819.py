import sys


def dfs():
    global answer
    if len(temp) == n:
        total = 0
        for i in range(n-1):
            total += abs(temp[i]-temp[i+1])
        answer = max(answer, total)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            temp.append(arr[i])
            dfs()
            visited[i] = False
            temp.pop()


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
temp = []
visited = [False] * n
answer = 0
dfs()


print(answer)
