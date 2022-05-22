import sys


def combination(arr, comb, r, index, depth):

    if r == 0:
        for i in comb:
            print(i, end=" ")
        print()
    elif depth == len(arr):
        return
    else:
        comb[index] = arr[depth]
        combination(arr, comb, r-1, index+1, depth+1)

        combination(arr, comb, r, index, depth+1)

while True:
    arr = list(map(int, sys.stdin.readline().split()))
    if len(arr) == 0:
        break

    comb = [0] * 6
    combination(arr[1:], comb, 6, 0, 0)
    print()