last = int(input())
i = 666
n = 0
answer = 0
while 1:
    if '666' in str(i) :
        n +=1
    if n == last:
        answer = i
        break
    i+=1
print(answer)