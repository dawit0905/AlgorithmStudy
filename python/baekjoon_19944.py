import sys


n, m = map(int, sys.stdin.readline().split())

if m < 3:
    print('NEWBIE!')
elif m <= n:
    print('OLDBIE!')
else:
    print('TLE!')
