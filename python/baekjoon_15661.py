import sys
from itertools import combinations


n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
row = [sum(i) for i in arr]
col = [sum(i) for i in zip(*arr)]
new_arr = [i + j for i, j in zip(row, col)]
total_sum = sum(new_arr) // 2
result = sys.maxsize
for num in range(1, n // 2 + 1):
    for combi in combinations(new_arr, num):
        result = min(result, abs(total_sum - sum(combi)))
        if result == 0:
            break

print(result)
