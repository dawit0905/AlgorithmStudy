import sys
n = int(sys.stdin.readline())
array = []
answer = 1

for i in range(n):
    array.append(int(sys.stdin.readline()))
front = array[-1]
for i in range(n-1):
    index = n - 2 - i
    if front < array[index]:
        front = array[index]
        answer +=1

print(answer)