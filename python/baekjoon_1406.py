import sys

_str = sys.stdin.readline().rstrip()
s1 = list(_str)
s2 = []

n = int(sys.stdin.readline())

for i in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd[0] == 'L':
        if len(s1) >= 1:
            s2.append(s1.pop(-1))
    elif cmd[0] == 'D':
        if len(s2) >= 1:
            s1.append(s2.pop(-1))
    elif cmd[0] == 'B':
        if len(s1) >= 1:
            s1.pop(-1)
    elif cmd[0] == 'P':
        s1.append(cmd.split(' ')[1])

s2.reverse()
print(*(s1+s2), sep='')

