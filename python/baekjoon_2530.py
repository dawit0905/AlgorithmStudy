import sys

h, m, s = map(int, sys.stdin.readline().split())
add_time = int(sys.stdin.readline())

total_time = h*60*60 + m*60 + s + add_time

hour = total_time // 3600 % 24
total_time %= 3600

minite = total_time // 60
total_time %= 60

second = total_time

print(hour, minite, second)
