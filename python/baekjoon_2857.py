import sys


answer = []
for i in range(5):
    s = sys.stdin.readline().strip()
    if s.find('FBI') != -1:
        answer.append(i+1)

if answer:
    print(*answer)
else:
    print("HE GOT AWAY!")