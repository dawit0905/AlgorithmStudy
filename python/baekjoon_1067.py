import sys

a = int(sys.stdin.readline())
x_list = list(map(int,sys.stdin.readline().split()))
y_list = list(map(int,sys.stdin.readline().split()))

data_sum = 0
data_sum_list=[]
count=0
for i in range(a) :
    for j in range(a):
        data_sum += x_list[count+j]*y_list[j]
    x_list.append(x_list[count])
    count +=1
    data_sum_list.append(data_sum)
    data_sum = 0
# print(data_sum_list)
print(max(data_sum_list))
