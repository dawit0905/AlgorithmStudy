import sys

text = sys.stdin.readline().rstrip().split("-")
answer = 0

for i in text[0].split("+"):
    answer += int(i)

for i in text[1:]:
    for j in i.split("+"):
        answer -= int(j)

print(answer)
