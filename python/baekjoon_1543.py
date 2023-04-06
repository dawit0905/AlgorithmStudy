import sys


s = sys.stdin.readline().strip()
sub_str = sys.stdin.readline().strip()

cnt = 0
i = 0
while i <= len(s) - len(sub_str):
    flag = True

    for j in range(len(sub_str)):
        if s[i+j] != sub_str[j]:
            flag = False
            break

    if flag:
        i += len(sub_str)
        cnt += 1
    else:
        i+=1


print(cnt)