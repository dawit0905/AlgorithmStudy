import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline()))

coins.sort(reverse=True)

count = 0
while k != 0:
    for coin in coins:
        if k >= coin:
            count = count + (k // coin)
            k = k % coin
            break

print(count)