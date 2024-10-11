from collections import deque
N = int(input())
arr = [
    list(map(int, input().split())) for _ in range(N)
]
visited = [
    [0] * N for _ in range(N)
]

def bfs(start):
    q = deque()
    q.append(start)
    nodes = [False] * N

    while q:
        cur = q.popleft()
        for to in range(N):
            if not nodes[to] and arr[cur][to] == 1:
                q.append(to)
                nodes[to] = True
                visited[start][to] = 1

# 정점 i 에서 갈 수 있는 노드들을 찾기 위해
for i in range(N):
    bfs(i)

for row in visited:
    print(*row)