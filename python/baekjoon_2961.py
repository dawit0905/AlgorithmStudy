import sys


def dfs(limit, depth, start):
    global answer

    if limit == depth:
        b_tmp, s_tmp = 1, 0
        for bitterness, sourness in sub_arr:
            b_tmp *= bitterness
            s_tmp += sourness

        answer = min(answer, abs(b_tmp-s_tmp))
        return

    for i in range(start, n):
        sub_arr.append(arr[i])
        dfs(limit, depth+1, i+1)
        sub_arr.pop()


n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a, b])

answer = sys.maxsize
sub_arr = []
for i in range(1, n+1):
    dfs(i, 0, 0)

print(answer)

''' 
bitterness 쓴맛
sourness 신맛
'''