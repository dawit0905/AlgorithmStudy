import sys
from itertools import combinations
from itertools import permutations


n = int(sys.stdin.readline())
arr = []
answer = sys.maxsize
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

comb_list = list(combinations(range(n), n//2))

for i in range(len(comb_list)//2):
    sum1 = 0
    sum2 = 0
    start = list(permutations(comb_list[i], 2))
    link = list(permutations(comb_list[len(comb_list)-i-1], 2))

    for j in range(len(start)):
        sum1 += arr[start[j][0]][start[j][1]]
        sum2 += arr[link[j][0]][link[j][1]]
    if answer > abs(sum1-sum2):
        answer = abs(sum1-sum2)

print(answer)
