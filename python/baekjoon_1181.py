import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(sys.stdin.readline().rstrip())

array = sorted(array, key= lambda x: (len(x), x))
temp = ''
for i in array:
    if temp == i:
        continue
    print(i)
    temp = i

'''
i
no
no
it
im
but
wont
more
more
wait
yours
cannot
hesitate
'''