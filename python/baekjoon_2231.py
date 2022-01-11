n = int(input())

answer = 1000001
for i in range(1,n+1):
    num = sum((map(int, str(i))))
    if n == num+i:
        answer = min(answer, i)
        break

if answer == 1000001:
    print(0)
else :
    print(answer)