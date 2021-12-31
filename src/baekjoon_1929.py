import sys, math
def prime(num):
    if num == 1: return False
    n = int(math.sqrt(num))
    for j in range(2,n+1):
        if num%j == 0:
            return False
    return True

nlist = list(map(int, sys.stdin.readline().split(' ')))

flag = False
for i in range(nlist[0],nlist[1]+1):
    flag = prime(i)
    if flag == True:
        print(i)