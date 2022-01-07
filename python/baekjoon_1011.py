import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    distinct = b-a
    count = 0
    while 1 :
        if distinct <= count*(count+1) :
            break
        count += 1
    if distinct <= count ** 2:
        print(count*2-1)
    else:
        print(count*2)