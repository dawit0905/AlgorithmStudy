'''
1
2
3

1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4

1 1 1
1 1 2
1 1 3
1 2 2
1 2 3
1 3 3
2 2 2
2 2 3
2 3 3
3 3 3
'''

def dfs(array,index):
    if len(array) == m:
        for i in array:
            print(i, end=" ")
        print()
        return
    for j in range(index,n+1):
        array.append(j)
        dfs(array,j)
        array.pop()

array = []
n, m = map(int, input().split())
dfs(array,1)

