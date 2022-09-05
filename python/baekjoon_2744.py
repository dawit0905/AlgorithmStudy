import sys


_str = sys.stdin.readline().rstrip()
result = ''
for i in range(len(_str)):
    if _str[i].isupper():
        result += _str[i].lower()
    else:
        result += _str[i].upper()

print(result)
