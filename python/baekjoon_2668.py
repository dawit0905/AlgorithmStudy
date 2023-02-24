import sys
from itertools import combinations
from collections import defaultdict


def dfs(u, visited):
    visited.add(u)
    checked[u] = 1
    for v in edges[u]:
        if v not in visited:
            dfs(v, visited.copy())
        else:
            result.extend(list(visited))
            return


sys.setrecursionlimit(int(10**6))
n = int(sys.stdin.readline())
edges = defaultdict(list)
for i in range(1, n+1):
    v = int(sys.stdin.readline())
    edges[v].append(i)

checked = [0] * (n+1)
result = []
for i in range(1, n+1):
    if not checked[i]:
        dfs(i, set([]))

result.sort()
print(len(result))
print(*result, sep='\n')






# n = int(sys.stdin.readline())
# arr = []
# for i in range(n):
#     arr.append(int(sys.stdin.readline()))
#
# combis = []
# for i in range(1, n+1):
#     combi = list(combinations(range(1, n+1), i))
#     combis.extend(combi)
#
# combis_set = set(combis)
# answer = 0
# answer_list = []
# for combi_set in combis_set:
#     differ_set = set()
#     for i in combi_set:
#         differ_set.add(arr[i-1])
#
#     if differ_set == set(combi_set):
#         if answer < len(differ_set):
#             answer = len(differ_set)
#             answer_list = list(differ_set)
#
# print(answer)
# print(*answer_list, sep="\n")
