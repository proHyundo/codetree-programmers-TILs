import sys

N = int(input())
dp = [sys.maxsize] * (N+1)
dp[1] = 0

if N > 1:
    dp[2] = 1
    for i in range(2, N+1):
        tmp3 = dp[i//3]+1 if i%3 == 0 else sys.maxsize
        tmp2 = dp[i//2]+1 if i%2 == 0 else sys.maxsize
        tmp1 = dp[i-1]+1
        dp[i] = min(tmp1, tmp2, tmp3)

print(dp[N])