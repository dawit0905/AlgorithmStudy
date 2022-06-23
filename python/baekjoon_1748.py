import sys

n = sys.stdin.readline().rstrip()
cnt = 0
comp = len(n)-1

for i in range(comp):
    cnt += 9 * (10 ** i) * (i + 1)
    i += 1

cnt += ((int(n) - (10 ** comp) + 1) * (comp + 1))
print(cnt)
