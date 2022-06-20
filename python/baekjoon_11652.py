import sys

n = int(sys.stdin.readline())
dictionary = {}

for i in range(n):
    a = int(sys.stdin.readline())

    if a not in dictionary:
        dictionary[a] = 1
    else:
        dictionary[a] += 1

arr = list(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))

temp = arr[0][1]
answer = arr[0][0]
for i in arr:
    if arr[0][1] != i[1]:
        break
    answer = min(answer, i[0])

print(answer)
