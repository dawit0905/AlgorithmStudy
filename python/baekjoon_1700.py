import sys


n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
multi_tab = []
answer = 0

for i in range(k):
    if arr[i] in multi_tab:
        continue

    # 멀티탭이 빈 공간이 있을 때
    elif len(multi_tab) < n:
        multi_tab.append(arr[i])
        continue

    # 멀티탭이 꽉찼을 때
    priority = []
    for tab in multi_tab:
        if tab in arr[i:]:
            priority.append(arr[i:].index(tab))
        else:
            priority.append(101)

    target = priority.index(max(priority))
    multi_tab.remove(multi_tab[target])
    multi_tab.append(arr[i])
    answer += 1

print(answer)