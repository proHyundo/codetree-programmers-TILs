N, K = map(int, input().split())
dp = [0] * (N + 1)
dp[0] = 1

for _ in range(K):
    for j in range(1, N + 1):
        dp[j] += dp[j - 1]

print(dp[N] % 1000000000)
