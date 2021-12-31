import sys

n = int(sys.stdin.readline())
data_sum_list = []
for i in range(n):
    a = int(sys.stdin.readline())
    data_sum = 0
    for j in range(a) :
        data = list(map(int, sys.stdin.readline().split(' ')))
        if max(data) > 0:
            data_sum += max(data)
    data_sum_list.append(data_sum)

for i in data_sum_list :
    print(i)