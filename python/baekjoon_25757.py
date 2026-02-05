import sys


N, game_type = sys.stdin.readline().split()
N = int(N)

name_set = set()
for i in range(N):
    name_set.add(sys.stdin.readline().strip())

cnt = len(name_set)
if game_type == 'Y':
    print(cnt)
elif game_type == 'F':
    print(cnt//2)
else:
    print(cnt//3)
