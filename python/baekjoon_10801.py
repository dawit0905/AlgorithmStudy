import sys


a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))
a_sum = 0
b_sum = 0

for i in range(10):
    if a_list[i] == b_list[i]:
        continue
    elif a_list[i] > b_list[i]:
        a_sum += 1
    else:
        b_sum += 1

if a_sum == b_sum:
    print('D')
elif a_sum > b_sum:
    print('A')
else:
    print('B')