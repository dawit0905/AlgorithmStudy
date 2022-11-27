import sys


s = sys.stdin.readline().rstrip()
s.lower()
cnt = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        cnt += 1
print(cnt)
