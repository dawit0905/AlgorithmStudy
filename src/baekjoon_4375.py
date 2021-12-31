def solve(n) :
    i = 1
    count = 1

    if n == 1:
        print(1)
        return
    while i != 0:
        i = (i * 10 + 1) % n
        count += 1
    print(count)

import sys

# number = map(int, sys.stdin.readline().split())
# for i in number:
#     solve(i)

solve(1)
# solve(2)
solve(3)
solve(7)
solve(9901)
# solve(4)
# solve(5)

