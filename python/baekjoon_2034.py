import sys


arr = ['C','','D','','E','F','','G','','A','','B']
start_point = [0,2,4,5,7,9,11]


t = int(sys.stdin.readline().strip())

command = []
for i in range(t):
    n = int(sys.stdin.readline())
    command.append(n)

answer = []
for i in start_point:
    now = i
    for j in command:
        now = (now+j) % 12
        if arr[now] == '':
            break
    else:
        answer.append([arr[i], arr[now]])

answer.sort()
for i, j in answer:
    print(i, j)