import sys


s = sys.stdin.readline().rstrip()

cnt = 0
temp = 0
answer = []
for i in s[::-1]:
    if cnt == 3:
        answer.append(temp)
        cnt = 0
        temp = 0
    temp += int(i) * 2**cnt
    cnt += 1

answer.append(temp)

result = ''

for i in answer[::-1]:
    result += str(hex(i))[2:]

print(result)

