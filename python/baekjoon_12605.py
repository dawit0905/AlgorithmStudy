import sys
n = int(sys.stdin.readline())

for i in range(1,n+1):
    array = list(map(str,sys.stdin.readline().split()))
    string = 'Case #'+str(i)+': '
    for j in range(len(array)):
        if j == len(array)-1:
            string += array[len(array) - j - 1]
        else :
            string += array[len(array)-j-1] + ' '
    print(string)
