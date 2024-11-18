import sys


n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
resource = list(map(int, sys.stdin.readline().split()))

state = resource[0]
answer = resource[0] * distance[0]
turn = 1
for i in range(1, len(resource)-1):
    state = min(state, resource[i])
    answer += state * distance[turn]
    turn += 1

print(answer)