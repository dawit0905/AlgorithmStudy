import sys


n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().rstrip()
    if 6 <= len(s) <= 9:
        print('yes')
    else:
        print('no')