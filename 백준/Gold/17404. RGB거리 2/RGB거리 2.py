
N = int(input())
costs = [
    list(map(int, input().split())) for _ in range(N)
]
total = 1000000 # 1000 * 1000

# 3가지 색깔 중 하나를 선택
for first_color in [0, 1, 2]:
    # 초기화
    dp = [
        [total] * 3 for _ in range(N)
    ]
    dp[0][first_color] = costs[0][first_color]

    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    # 첫 색깔과 마지막 색깔도 달라야 한다
    for last_color in [0, 1, 2]:
        if first_color != last_color:
            total = min(total, dp[N-1][last_color])

print(total)