N = int(input())

dp = [
    [0] * 10 for _ in range(N+1)
]

# dp[1] = [1] * 10 으로 대체 가능
for i in range(10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])

print(sum(dp[N]) % 10007)
