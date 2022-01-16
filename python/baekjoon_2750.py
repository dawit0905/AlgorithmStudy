import sys

n = int(sys.stdin.readline().rstrip())
asdf = []
for i in range(n):
    asdf.append(int(sys.stdin.readline().rstrip()))

asdf.sort()

for i in asdf :
    print(i)