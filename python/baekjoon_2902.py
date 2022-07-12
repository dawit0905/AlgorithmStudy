import sys

str_list = sys.stdin.readline().rstrip().split('-')
answer = ''

for i in str_list:
    answer += i[0]

print(answer)
