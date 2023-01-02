import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
# 영식 요금제
sum1 = 0
for i in arr:
    if i // 30 == 0:
        sum1 += 10
    else:
        sum1 += 10 + 10 * (i // 30)
# 민식 요금제
sum2 = 0
for i in arr:
    if i // 60 == 0:
        sum2 += 15
    else:
        sum2 += 15 + 15 * (i // 60)

if sum1 == sum2:
    print(f"Y M {sum1}")
elif sum1 < sum2:
    print(f"Y {sum1}")
else:
    print(f"M {sum2}")


