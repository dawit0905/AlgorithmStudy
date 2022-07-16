import sys



'''
A -> B
B -> BA

A 0 1
B 1 0
BA 1 1
BAB 1 2
BABBA 2 3
BABBABAB 3 5
BABBABABBABBA 5 8 
'''
k = int(sys.stdin.readline())
AB_list = [[0,0] for _ in range(48)]
AB_list[1] = [1,0]
AB_list[2] = [0,1]

for i in range(3, k+2):
    AB_list[i] = [AB_list[i-1][0] + AB_list[i-2][0], AB_list[i-1][1] + AB_list[i-2][1]]

print(AB_list[k+1][0], AB_list[k+1][1])

