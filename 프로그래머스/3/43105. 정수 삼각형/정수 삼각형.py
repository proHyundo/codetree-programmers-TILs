def solution(triangle):
    h = len(triangle)

    dp = [
        [0] * i for i in range(1, h+1)
    ]

    dp[0][0] = triangle[0][0]

    for i in range(1, h):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        dp[i][i] = dp[i-1][i-1] + triangle[i][i]

    if h >= 3:
        for i in range(2, h):
            for j in range(1, i):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

    return max(dp[h-1])