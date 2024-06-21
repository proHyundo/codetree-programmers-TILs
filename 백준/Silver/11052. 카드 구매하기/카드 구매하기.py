N = int(input())
p = [0] + list(map(int, input().split()))
dp = [
    [0] * (N+1) for _ in range(N+1)
]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j]
        if 0 <= j - i:
            dp[i][j] = max(dp[i-1][j-i] + p[i], dp[i][j-i] + p[i], dp[i][j])

print(dp[N][N])
