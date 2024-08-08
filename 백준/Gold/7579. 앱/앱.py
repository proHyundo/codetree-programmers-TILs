N, M = map(int, input().split()) # N개의 앱 활성화
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
max_cost = sum(costs)+1
dp = [
    [0] * max_cost for _ in range(N+1)
]
answer = max_cost

for i in range(1, N+1):
    m, c = memories[i-1], costs[i-1]
    for j in range(0, max_cost):
        if j < c:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c] + m)

        if dp[i][j] >= M:
            answer = min(answer, j)

print(dp)

print(answer if M != 0 else 0)