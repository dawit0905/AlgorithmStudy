from math import factorial

n = int(input())
fac_n = factorial(n)

cnt = 0
a = str(fac_n)
for i in range(1, len(a) + 1):
    if a[-i] == '0':
        cnt += 1
    else:
        break
print(cnt)
