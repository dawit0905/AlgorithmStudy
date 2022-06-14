import sys

n = int(sys.stdin.readline())
dic = {}
for i in range(n):
    bookName = sys.stdin.readline().rstrip()
    if bookName not in dic:
        dic[bookName] = 1
    else:
        dic[bookName] += 1

temp = sorted(dic.items(), key=lambda x: x[1], reverse=True)

max_num = temp[0][1]
arr = []
for i in temp:
    if max_num == i[1]:
        max_num = i[1]
    else:
        break
    arr.append(i[0])
arr.sort()
print(arr[0])
