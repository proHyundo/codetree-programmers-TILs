from collections import deque

M, N, H = map(int, input().split())  # 가로, 세로, 높이
arr = [
    [
        list(map(int, input().split())) for _ in range(N)
    ] for _ in range(H)
]


def bfs():
    q = deque()
    tomatoes = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if arr[h][n][m] == 1:
                    q.append((h, n, m))
                elif arr[h][n][m] == 0:
                    tomatoes += 1

    while q:
        ch, cn, cm = q.popleft()

        for dh, dn, dm in [(0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
            nh, nn, nm = ch + dh, cn + dn, cm + dm
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and arr[nh][nn][nm] == 0:
                q.append((nh, nn, nm))
                arr[nh][nn][nm] = arr[ch][cn][cm] + 1
                tomatoes -= 1

    if tomatoes == 0:
        return arr[ch][cn][cm] - 1
    else:
        return -1


print(bfs())
