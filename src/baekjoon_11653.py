import sys, math


a = int(sys.stdin.readline())

for i in range(2,int(math.sqrt(a))+1,1) :
    while (a % i == 0) :
        print(i)
        a /= i

if a!=1 :
    print(int(a))
