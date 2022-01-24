'''
1
2
3

1 2
1 3
1 4
2 3
2 4
3 4

1 2 3 4
'''

def dfs(array,index):
    if len(array) == m:
        for i in array:
            print(i, end=" ")
        print()
        return
    for j in range(index,n+1):
        if j not in array :
            array.append(j)
            dfs(array,j+1)
            array.pop()

array = []
n, m = map(int, input().split())
dfs(array,1)

