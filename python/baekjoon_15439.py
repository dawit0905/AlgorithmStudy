import sys
from itertools import combinations


n = int(sys.stdin.readline())
arr = [i for i in range(1, n+1)]
combi = list(combinations(arr, 2))
print(len(combi)*2)
