from collections import deque
F, S, G, U, D = map(int, input().split())  # F : 총 층수, S : 현재 위치 , G : 스타트링크 위치
v = [-1] * 2000001


def bfs(start, end):
    q = deque()
    q.append(start)
    v[start] = 0

    while q:
        c = q.popleft()
        if c == end:
            return v[G]

        for next_floor in (c+U, c-D):
            if 1 <= next_floor <= F and v[next_floor] == -1: # 다음 층 수가 총 층수 범위 내, 방문한적 없음
                q.append(next_floor)
                v[next_floor] = v[c] + 1

    return "use the stairs"


print(bfs(S, G))
