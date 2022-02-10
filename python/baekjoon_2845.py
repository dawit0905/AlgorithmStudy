l,p = map(int, input().split())
array = list(map(int, input().split()))
answer = []

for i in array:
    answer.append(i-(l*p))

print(*answer)
