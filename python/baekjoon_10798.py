import sys


arr = [sys.stdin.readline().split() for _ in range(5)]
answer = [[] for _ in range(15)]

for i in arr:
    for idx, element in enumerate(''.join(i)):
        answer[idx].append(element)


for i in answer:
    print(*i, sep="", end='')
