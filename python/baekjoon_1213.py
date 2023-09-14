import sys


s = list(sys.stdin.readline().strip())

dic = {}
for i in s:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

flag = 0
alph = ''
for key in dic.keys():
    if dic[key] % 2 == 1:
        flag += 1
        alph = key
        if flag > 1:
            print("I'm Sorry Hansoo")
            exit(0)

answer = ''
for key in sorted(dic.keys()):
    for i in range(dic[key]//2):
        answer += key


answer += alph + answer[::-1]
print(answer)
