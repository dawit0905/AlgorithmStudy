import sys

_str = sys.stdin.readline().rstrip()

flag = True

for i in range(len(_str)//2):
    if _str[i] != _str[(len(_str)-1)-i]:
        flag = False
        break

if flag:
    print(1)
else:
    print(0)