N, K = map(int,input().split())

count = 0
for h in range(N+1):
    if h < 10:
        hour = '0' + str(h)
    else :
        hour = str(h)
    for m in range(60):
        if m < 10:
            min = '0' + str(m)
        else :
            min = str(m)
        for s in range(60):
            if s < 10:
                sec = '0' + str(s)
            else :
                sec = str(s)
            if str(K) in str(hour)+str(min)+str(sec):
                count+=1

print(count)