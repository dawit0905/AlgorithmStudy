import sys


tc = int(sys.stdin.readline())

for i in range(tc):
    n = int(sys.stdin.readline())
    a_sum = 0
    b_sum = 0
    for j in range(n):
        a, b = map(float, sys.stdin.readline().split())
        a_sum += a
        b_sum += a * b

    GPA = b_sum / a_sum
    print(int(a_sum), '%.1f' % GPA)