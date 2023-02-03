import sys
import string


dic = {}
alphabets = string.ascii_uppercase
for i in range(len(alphabets)):
    dic[alphabets[i]] = alphabets[(i-3) % 26]

s = sys.stdin.readline().rstrip()

for i in s:
    print(dic[i], end="")
