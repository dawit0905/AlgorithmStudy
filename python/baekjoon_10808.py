import sys


word = sys.stdin.readline().rstrip()
alphabet_list = [0] * 26

for i in word:
    alphabet_list[ord(i)-97] += 1


print(*alphabet_list)