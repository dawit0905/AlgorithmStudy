import sys


n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
cnt = 1

idx = 0
while idx < n:
    if s[idx] == 'S':
        cnt += 1

    elif s[idx] =='L':
        cnt += 1
        idx += 1

    idx += 1


print(n) if cnt > n else print(cnt)
