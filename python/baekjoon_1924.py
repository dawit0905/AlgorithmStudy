import sys

x, y = map(int, sys.stdin.readline().split())

dict = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}
total = y
for i in range(1, x):
    total += dict[i]

if total%7 == 1:
    print('MON')
elif total%7 == 2:
    print('TUE')
elif total%7 == 3:
    print('WED')
elif total%7 == 4:
    print('THU')
elif total%7 == 5:
    print('FRI')
elif total%7 == 6:
    print('SAT')
else:
    print('SUN')
