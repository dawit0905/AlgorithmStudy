'''
1
2
3

1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
'''

def dfs(array):
    if len(array) == m:
        for i in array:
            print(i, end=" ")
        print()
        return
    for j in range(1,n+1):
        if j not in array:
            array.append(j)
            dfs(array)
            array.pop()

array = []
n, m = map(int, input().split())
dfs(array)


