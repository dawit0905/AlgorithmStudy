import sys

n = int(sys.stdin.readline())
index = 1
array = []
answer = []
flag = 1
for i in range(n):
    input_data = int(sys.stdin.readline())

    while index <= input_data:
        array.append(index)
        answer.append('+')
        index += 1

    if array[-1] == input_data:
        array.pop()
        answer.append('-')
    else :
        print('NO')
        flag = 0
        break

if flag == 1:
    for i in answer:
        print(i)

