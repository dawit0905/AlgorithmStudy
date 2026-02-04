import sys

p = int(sys.stdin.readline())

for _ in range(p):
    arr = list(map(int, sys.stdin.readline().split()))
    t = arr[0]
    heights = arr[1:]
    line = []
    steps = 0

    for h in heights:
        inserted = False
        for i in range(len(line)):
            if line[i] > h:
                steps += len(line) - i
                line.insert(i, h)
                inserted = True
                break
        if not inserted:
            line.append(h)

    print(f"{t} {steps}")
