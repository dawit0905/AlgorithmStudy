import sys

n = sys.stdin.readline()[0] # 개행문자 삭제
nlist = list(map(int , sys.stdin.readline().split(' ')))

count = 0
i = 0
j = 0
for i in nlist:
    for j in range(2,i+1):
        if i == j:
            count += 1
        if i%j == 0:
            break

print(count)