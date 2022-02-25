import sys

n, m = map(int, sys.stdin.readline().split())
answer = []
dic = dict()

for i in range(n):
    name = sys.stdin.readline().rstrip()
    dic[name] = 1

for j in range(m):
    name = sys.stdin.readline().rstrip()
    if name in dic:
        answer.append(name)
        dic[name] += 1

print(len(answer))
answer.sort()
for i in answer:
    print(i)
