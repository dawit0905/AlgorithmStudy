import sys

n = int(sys.stdin.readline())
city = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
postcost = cost[0]
total = cost[0] * city[0]

for i in range(1, n-1):
    if cost[i] < postcost:
        postcost = cost[i]
    total += postcost * city[i]

print(total)