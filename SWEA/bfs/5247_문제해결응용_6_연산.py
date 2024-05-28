# DFS 으로 풀이하려 했으나 재귀호출 깊이 제한, 시간 제한으로 불가했다. 따라서 BFS으로 풀이
from collections import deque


def bfs():
    q = deque()
    q.append(N)
    v = [-1] * 1000001
    v[N] = 0

    while q:
        cur = q.popleft()

        if cur == M:
            return v[M]

        # 아래 if문 4개를 다음과 같이 for문으로도 해결 가능하다.
        # for n in ((cur+1), (cur-1), (cur*2), (cur-10)):
        if cur + 1 <= 1000000 and v[cur + 1] == -1:
            q.append(cur + 1)
            v[cur + 1] = v[cur] + 1
        if cur - 1 <= 1000000 and v[cur - 1] == -1:
            q.append(cur - 1)
            v[cur - 1] = v[cur] + 1
        if cur * 2 <= 1000000 and v[cur * 2] == -1:
            q.append(cur * 2)
            v[cur * 2] = v[cur] + 1
        if cur - 10 <= 1000000 and v[cur - 10] == -1:
            q.append(cur - 10)
            v[cur - 10] = v[cur] + 1

    return v[M]


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{test_case}', bfs())
