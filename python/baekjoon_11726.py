n = int(input())
data = [1,2,3]
for i in range(3,n):
    data.append(data[i-1] + data[i-2])
answer = data[n-1]
print(answer%10007)