from collections import deque
def solution(maps):
    h = len(maps)
    w = len(maps[h-1])

    def bfs():
        q = deque()
        q.append((0, 0))
        v = [
            [0] * w for _ in range(h)
        ]
        v[0][0] = 1
        while q:
            ci, cj = q.popleft()
            for di, dj in zip([0,1,0,-1], [1,0,-1,0]):
                ni, nj = di + ci, dj + cj
                if 0 <= ni < h and 0 <= nj < w and maps[ni][nj] != 0 and v[ni][nj] == 0:
                    q.append((ni, nj))
                    v[ni][nj] = v[ci][cj] + 1
        return -1 if v[h-1][w-1] == 0 else v[h-1][w-1]
    return bfs()