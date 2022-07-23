import sys

n, k = map(int, sys.stdin.readline().split())
cnt = 1
removed_list = []
for i in range(2, n+1):
    j = i
    while j <= n:
        if j not in removed_list:
            if cnt == k:
                print(j)
                exit(0)
            cnt += 1
        removed_list.append(j)
        j += i
