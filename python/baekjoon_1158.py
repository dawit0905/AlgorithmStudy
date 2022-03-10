n, k = map(int, input().split())

answer = []
arr = [i for i in range(1, n+1)]
index = 0
for i in range(n):
    index = index + (k-1)
    if index != 0:
        index = index % len(arr)
    answer.append(str(arr.pop(index)))

print("<", ", ".join(answer), ">", sep='')
