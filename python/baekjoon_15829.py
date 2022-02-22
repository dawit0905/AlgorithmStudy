r = 31
m = 1234567891

l = int(input())
arr = list(input())
answer = 0
for i in range(l):
    answer += (ord(arr[i])-96) *(r**i)

print(answer%m)