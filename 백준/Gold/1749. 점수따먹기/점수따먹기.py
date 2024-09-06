import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = [
    list(map(int, input().split())) for _ in range(N)
]
dp = [
    [-400000000] * (M+1) for _ in range(N+1)
]

ans = -400000000

# 미리 각 좌표마다 누적합을 구해 놓기
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + board[i - 1][j - 1]


# x1, y1 좌표 부터 x2, y2 좌표 까지의 합
for x1 in range(1, N+1):
    for y1 in range(1, M+1):
        for x2 in range(x1, N+1):
            for y2 in range(y1, M+1):
                ans = max(ans, dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])

print(ans)