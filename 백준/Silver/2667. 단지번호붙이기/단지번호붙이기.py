from collections import deque
N = int(input())
board = [
    list(map(int, input())) for _ in range(N)
]
checked = [
    [False] * N for _ in range(N)
]
ans = []


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    checked[si][sj] = True
    cnt = 1

    while q:
        ci, cj = q.popleft()

        for di, dj in zip([0,1,0,-1], [1,0,-1,0]):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 1 and not checked[ni][nj]:
                q.append((ni, nj))
                checked[ni][nj] = True
                cnt += 1

    return cnt


for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not checked[i][j]:
            ans.append(bfs(i, j))

print(len(ans))
for ele in sorted(ans):
    print(ele)
