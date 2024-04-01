import sys

N = int(input())
dp = [0] * 1000001
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N+1):
    min_cnt = sys.maxsize
    if i % 3 == 0:
        min_cnt = min(min_cnt, dp[i//3]+1)
    if i % 2 == 0:
        min_cnt = min(min_cnt, dp[i//2]+1)

    min_cnt = min(min_cnt, dp[i-1]+1)

    dp[i] = min_cnt

print(dp[N])
