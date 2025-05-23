from bisect import bisect_left, bisect_right
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))
card.sort()

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value) # 해당수가 있는 오른쪽 인덱스
    left_index = bisect_left(a, left_value) # 해당수가 있는 왼쪽 인덱스
    return right_index - left_index


for i in range(len(test)):
    print(count_by_range(card, test[i], test[i]), end=' ')