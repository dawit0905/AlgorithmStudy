import sys


n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

A_cnt = 0
B_cnt = 0

for i in s:
    if i == 'A':
        A_cnt += 1
    else:
        B_cnt += 1

if A_cnt == B_cnt:
    print('Tie')
elif A_cnt > B_cnt:
    print('A')
else:
    print('B')