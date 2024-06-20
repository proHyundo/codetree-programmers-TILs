from collections import deque

arr = [list(input()) for _ in range(5)]
ans = 0


def check(tlst):
    x, y = tlst[0]
    q = deque()
    q.append((x, y))

    v = [[False] * 5 for _ in range(5)]
    v[x][y] = True

    cnt = 1

    while q:
        cx, cy = q.popleft()
        for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            nx, ny = dx + cx, dy + cy
            if (nx, ny) in tlst and not v[nx][ny]:
                q.append((nx, ny))
                v[nx][ny] = True
                cnt += 1

    if cnt == 7:
        return True
    return False

def dfs(n, cnt, scnt, lst):
    global ans
    if cnt > 7:
        return
    if n == 25:
        if cnt == 7 and scnt >= 4:
            if check(lst):
                ans += 1
        return

    dfs(n + 1, cnt + 1, scnt + (1 if arr[n // 5][n % 5] == 'S' else 0), lst + [(n // 5, n % 5)])
    dfs(n + 1, cnt, scnt, lst)


dfs(0, 0, 0, [])

print(ans)
