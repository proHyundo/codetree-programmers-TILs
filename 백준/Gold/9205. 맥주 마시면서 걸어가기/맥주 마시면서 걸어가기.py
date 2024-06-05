from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())  # 편의점 개수
    house = tuple(map(int, input().split()))
    stores = []
    for _ in range(N):
        stores.append(tuple(map(int, input().split())))
    v = [False] * N
    rock = tuple(map(int, input().split()))


    def bfs(h, r):
        q = deque()
        q.append(h)
        rx, ry = r

        while q:
            cx, cy = q.popleft()
            if abs(rx-cx) + abs(ry-cy) <= 1000:
                return 'happy'

            for i in range(N):
                if not v[i] and abs(stores[i][0] - cx) + abs(stores[i][1] - cy) <= 1000:
                    q.append(stores[i])
                    v[i] = True

        return 'sad'


    print(bfs(house, rock))
