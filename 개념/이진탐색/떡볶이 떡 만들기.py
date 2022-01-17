n, m = map(int,input().split())
array = list(map(int,input().split()))

'''
4 6
19 15 10 17
16 -> 3 1 = 4
15 -> 4 2 = 6
14 -> 5 1 3 = 9
13 -> 6 2 4 = 12
자르는 길이가 길어지면 떡을 적게 가져가고
자르는 길이가 짧아지면 떡을 많이 가져간다. 
'''
start = 0
end = max(array)

result = 0
while(start <= end):
    mid = (start + end) // 2
    total = 0

    for i in array :
        if i > mid:
            total = total + i - mid

    if total < m:
        end = mid-1
    elif total >= m :
        start = mid+1
        result = mid


print(result)
