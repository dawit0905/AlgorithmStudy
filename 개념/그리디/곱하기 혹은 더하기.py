array = list(map(int,input()))


result = int(array[0])
for i in range(1,len(array)):
    if int(result+array[i]) > result*array[i]:
        result += array[i]
    else :
        result *= array[i]

print(result)
