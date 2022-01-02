import sys

answer_list = []
data_list = []
while 1 :
    temp_list = list(map(int, sys.stdin.readline().split()))
    if (temp_list == [0,0,0]) :
        break
    else :
        data_list.append(temp_list)

for i in range(len(data_list)) :
    data_list[i].sort()
    if data_list[i][0] ** 2 + data_list[i][1] ** 2 == data_list[i][2] ** 2:
        print('right')
    else :
        print('wrong')

