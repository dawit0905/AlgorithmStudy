import sys
n = int(sys.stdin.readline())
answer = ''

for i in range(n):
    string = list(sys.stdin.readline().rstrip())
    sum = 0
    for j in string:
        if j == '(':
            sum += 1
        elif j == ')' :
            sum -= 1
        if sum < 0 :
            print('NO')
            break
    if sum == 0:
        print('YES')
    elif sum > 0 :
        print('NO')


