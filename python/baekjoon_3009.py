import sys
data_list = []
x_list = []
y_list = []
answer = []
for i in range(3):
    data_list.append(list(map(int, sys.stdin.readline().split(' '))))
    x_list.append(data_list[i][0])
    y_list.append(data_list[i][1])

x_list.sort()
y_list.sort()
if x_list[0] == x_list[1] :
    answer.append(x_list[-1])
else :
    answer.append(x_list[0])
if y_list[0] == y_list[1] :
    answer.append(y_list[-1])
else :
    answer.append(y_list[0])
print("%d %d"%(answer[0],answer[1]))

