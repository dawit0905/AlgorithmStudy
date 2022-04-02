
n = int(input())
if (n//2)%2 == 1:
    first = 1
    second = 0
else:
    first = 0
    second = 1
arr = [[first] * n for _ in range(n)]
if n == 3:
    arr[1][1] = 0
    excute = 0
elif n == 1:
    excute = 0
elif n == 5:
    excute = 1
else:
    excute = (n-5)//2 + 1

for k in range(1, excute+1):
    if arr[k-1][k-1] == 1:
        flag = 0
    else:
        flag = 1
    for i in range(k,n-k):
        for j in range(k,n-k):
            if n//2 == i and n//2 == j:
                arr[i][j] = 0
            else:
                arr[i][j] = flag

    if flag == 0:
        flag = 1
    else:
        flag = 0

for i in range(n):
    for j in range(n):
        print(arr[i][j], end= " ")
    print()