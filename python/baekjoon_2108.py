import sys

n = int(sys.stdin.readline())

vals = []

for _ in range(n):
    temp = int(sys.stdin.readline())
    vals.append(temp)

vals.sort()


def average(vals):
    return round(sum(vals)/len(vals))

def center(vals):
    return vals[len(vals)//2]

def freq(vals):
    import collections
    cnt = collections.Counter(vals).most_common()

    if len(vals) > 1:
        if cnt[0][1] == cnt[1][1]:
            return cnt[1][0]
        else:
            return cnt[0][0]
    else :
        return cnt[0][0]

def range(vals):
    return vals[-1] - vals[0]

print(average(vals))
print(center(vals))
print(freq(vals))
print(range(vals))
