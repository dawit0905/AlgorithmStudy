import sys


s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

s_len = len(s)
t_len = len(t)
length = t_len - s_len

for i in range(t_len, t_len - length, -1):
    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]

if s == t:
    print(1)
else:
    print(0)
