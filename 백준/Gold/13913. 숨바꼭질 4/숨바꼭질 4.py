from collections import deque
import sys
sys.setrecursionlimit(10**8)
N, K = map(int, input().split())
R = 100000 * 2
v = [-1] * (R+1)

def bfs(start, end):
    q = deque()
    q.append(start)
    v[start] = (0, start) # v[현재위치] = [최소이동횟수, 이전위치]

    while q:
        cur = q.popleft()
        if cur == end:
            return v[end]
        cnt = v[cur][0]
        # 다음위치가 방문한 적 없거나, 방문했더라도 이동횟수가 더 적다면, 갱신 후 큐에 삽입
        if 0 <= cur-1 <= R and (v[cur-1] == -1 or v[cur-1][0] > cnt):
            v[cur-1] = (cnt+1, cur)
            q.append(cur-1)
        if 0 <= cur+1 <= R and (v[cur+1] == -1 or v[cur+1][0] > cnt):
            v[cur+1] = (cnt+1, cur)
            q.append(cur+1)
        if 0 <= cur*2 <= R and (v[cur*2] == -1 or v[cur*2][0] > cnt):
            v[cur*2] = (cnt+1, cur)
            q.append(cur*2)

result = bfs(N, K)
total_cnt = result[0]
paths = [K]

def find_path(n):
    cnt, parent = v[n]
    if cnt == 0:
        return
    paths.append(parent)
    find_path(parent)

find_path(K)
print(total_cnt)
print(*paths[::-1])