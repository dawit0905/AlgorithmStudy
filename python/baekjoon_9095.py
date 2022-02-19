n = int(input())
tc = [1, 2, 4]
for i in range(3, 10):
    tc.append(tc[i - 3] + tc[i - 2] + tc[i - 1])
for i in range(n):
    number = int(input())
    print(tc[number - 1])