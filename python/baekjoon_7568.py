import sys
n = int(input())

array = []
flag = [1 for _ in range(n)]
for _ in range(n):
    array.append(list(map(int, input().split() ) ) )

for i in range(n):
    for j in range(n):
        if i == j :
            continue
        if array[i][0] < array[j][0] and array[i][1] < array[j][1] :
            flag[i] += 1

for i in range(n):
    print(flag[i],end= ' ')