import sys


n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())

answer = ''
cnt = 0
for i in range(m):
    tmp = {'A':0, 'T':0, 'G':0, 'C':0}
    for j in range(n):
        tmp[arr[j][i]] += 1

    ttp = list(tmp.items())
    ttp.sort(key=lambda x: (-int(x[1]), x[0]))
    answer += ttp[0][0]
    cnt += n - ttp[0][1]

print(answer)
print(cnt)