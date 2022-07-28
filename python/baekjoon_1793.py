import sys


dp = [0] * 251
dp[0] = 1
dp[1] = 1

for i in range(2, 251):
    dp[i] = dp[i-1]+2 * dp[i-2]


while True:
    try:
        print(dp[int(sys.stdin.readline())])
    except:
        break