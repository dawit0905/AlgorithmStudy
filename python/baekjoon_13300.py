import sys


n, k = map(int, sys.stdin.readline().split())
arr = list()
set_temp = set()
for i in range(n):
    s, y = map(int, sys.stdin.readline().split())
    arr.append((s, y))
    set_temp.add((s, y))

answer = 0
for i in set_temp:
    temp = arr.count(i)

    if (temp % k == 0):
        answer += temp / k
    else:
        answer += temp // k + 1
        
# answer += len(set_temp)
print(int(answer))
