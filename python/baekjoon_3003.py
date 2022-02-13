data = list(map(int, input().split()))
answer = [1,1,2,2,2,8]

for i in range(len(answer)):
    answer[i] = answer[i] - data[i]

print(*answer)