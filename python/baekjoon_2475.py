array = list(map(int, input().rstrip().split()))
total = 0
for i in array:
    total = total + pow(i, 2)

print(total % 10)
