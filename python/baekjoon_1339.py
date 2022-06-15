import sys

n = int(sys.stdin.readline())
alphabets = []
dic = {}
numbers = []
for i in range(n):
    alphabets.append(sys.stdin.readline().rstrip())

for i in range(n):
    for j in range(len(alphabets[i])):
        if alphabets[i][j] in dic:
            dic[alphabets[i][j]] += 10 ** (len(alphabets[i])-j-1)
        else:
            dic[alphabets[i][j]] = 10 ** (len(alphabets[i])-j-1)

for i in dic.values():
    numbers.append(i)

numbers.sort(reverse=True)
num = 9
total = 0
for i in numbers:
    total += num * i
    num -= 1

print(total)

