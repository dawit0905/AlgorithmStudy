import sys

dic = dict()
dic2 = dict()
n, m = map(int, sys.stdin.readline().rstrip().split())

for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    dic[name] = str(i)
    dic2[str(i)] = name

for j in range(m):
    a = sys.stdin.readline().rstrip()
    if a.isdigit():
        print(dic2[a])
    else:
        print(dic[a])
