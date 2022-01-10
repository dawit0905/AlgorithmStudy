import sys
n, m = map(int,sys.stdin.readline().rstrip().split())

list = list(map(int,sys.stdin.readline().rstrip().split()))
answer = 0
for i in range(n):
    for j in range(i+1,n):
        for t in range(j+1,n):
            if list[i]+list[j]+list[t] > m:
                continue
            answer = max(answer, list[i]+list[j]+list[t])

print(answer)