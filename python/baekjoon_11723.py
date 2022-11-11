import sys

m = int(sys.stdin.readline())
bit = 0

for _ in range(m):
    temp = sys.stdin.readline().strip().split()

    if len(temp) == 1:
        if temp[0] == "all":
            bit = (1<<20) - 1
        else:
            bit = 0
    else:
        func, x = temp[0], temp[1]
        x = int(x) - 1

        if func == "add":
            bit = bit | (1<<x)
        elif func == "remove":
            bit = bit & ~(1 << x)
        elif func == "check":
            if bit & (1 << x) == 0:
                print(0)
            else:
                print(1)
        elif func == "toggle":
            bit = bit ^ (1<<x)