import sys

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = sys.maxsize
visited = [False] * N


def dfs(row, sm):
    global ans
    if row == N:
        ans = min(ans, sm)
        return
    for j in range(0, N):
        if not visited[j]:
            visited[j] = True
            dfs(row + 1, sm + board[row][j])
            visited[j] = False


dfs(0, 0)
print(ans)
