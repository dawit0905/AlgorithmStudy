import sys

b = int(sys.stdin.readline())
testcase = []

for i in range(b):
    testcase.append(int(sys.stdin.readline()))


# 에라토스테네스의 체
n=10000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

for i in testcase:
    p, q = i//2, i//2
    while True :
        if a[p] == True and a[q] == True:
            print("%d %d" %(p,q))
            break
        p -= 1
        q += 1
