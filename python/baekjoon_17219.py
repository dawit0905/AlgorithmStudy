import sys

n, m = map(int, sys.stdin.readline().split())
dic = {}

for i in range(n):
    site, passwd = map(str, sys.stdin.readline().rstrip().split())
    dic[site] = passwd

for j in range(m):
    site = sys.stdin.readline().rstrip()
    print(dic[site])
