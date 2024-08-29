R, C = map(int, input().split())
answer = 0
board = [
    list(input()) for _ in range(R)
]
visited = [
    [False] * C for _ in range(R)
]
alpha_lst = [False] * 26


# 65 ~ 90
def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)
    for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and not alpha_lst[ord(board[nx][ny]) - 65]:
            visited[nx][ny] = True
            alpha_lst[ord(board[nx][ny]) - 65] = True
            dfs(nx, ny, cnt + 1)
            alpha_lst[ord(board[nx][ny]) - 65] = False
            visited[nx][ny] = False

visited[0][0] = True
alpha_lst[ord(board[0][0]) - 65] = True
dfs(0, 0, 1)

print(answer)