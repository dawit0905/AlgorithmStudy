import sys


n = int(sys.stdin.readline())
dic = {}
for i in range(n):
    s = sys.stdin.readline().strip().split('.')
    extension = s[1]
    if extension in dic:
        dic[extension] += 1
    else:
        dic[extension] = 1

for i in sorted(list(dic.items()), key = lambda x : x[0]):
    print(i[0], i[1])