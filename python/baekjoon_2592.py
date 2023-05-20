import sys
from collections import Counter

arr = [int(sys.stdin.readline()) for _ in range(10)]
print(sum(arr)//10)
cnt = Counter(arr).most_common(1)[0]
print(cnt[0])