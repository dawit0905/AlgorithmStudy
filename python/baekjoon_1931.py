import sys

n = int(sys.stdin.readline())
array = []
for i in range(n):
    start, end = (map(int, sys.stdin.readline().split()))
    array.append((end, start))

array.sort()

count = 0
end_time = 0
for end, start in array:
    if start >= end_time:
        end_time = end
        count += 1

print(count)
