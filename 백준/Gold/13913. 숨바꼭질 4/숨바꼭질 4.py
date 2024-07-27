"""
개선된 풀이
"""
from collections import deque

N, K = map(int, input().split())
R = 100001
v = [False] * R
c = [0] * R

def bfs(start, end):
    q = deque()
    q.append(start)

    while q:
        cur = q.popleft()
        if cur == end:
            return v[end]

        for nxt in (cur-1, cur+1, cur*2):
            if 0 <= nxt < R and not v[nxt]:
                v[nxt] = v[cur] + 1
                q.append(nxt)
                c[nxt] = cur

total_cnt = bfs(N, K)
paths = []

def find_path(end):
    before = end
    for _ in range(total_cnt+1):
        paths.append(before)
        before = c[before]


find_path(K)
print(total_cnt if total_cnt else 0)
print(*paths[::-1])

"""
최초 풀이
"""
# from collections import deque
# import sys
# sys.setrecursionlimit(10**8)
# N, K = map(int, input().split())
# R = 100000 * 2
# v = [-1] * (R+1)
#
# def bfs(start, end):
#     q = deque()
#     q.append(start)
#     v[start] = (0, start) # v[현재위치] = [최소이동횟수, 이전위치]
#
#     while q:
#         cur = q.popleft()
#         if cur == end:
#             return v[end]
#         cnt = v[cur][0]
#         # 다음위치가 방문한 적 없거나, 방문했더라도 이동횟수가 더 적다면, 갱신 후 큐에 삽입
#         if 0 <= cur-1 <= R and (v[cur-1] == -1 or v[cur-1][0] > cnt):
#             v[cur-1] = (cnt+1, cur)
#             q.append(cur-1)
#         if 0 <= cur+1 <= R and (v[cur+1] == -1 or v[cur+1][0] > cnt):
#             v[cur+1] = (cnt+1, cur)
#             q.append(cur+1)
#         if 0 <= cur*2 <= R and (v[cur*2] == -1 or v[cur*2][0] > cnt):
#             v[cur*2] = (cnt+1, cur)
#             q.append(cur*2)
#
# result = bfs(N, K)
# total_cnt = result[0]
# paths = [K]
#
# def find_path(n):
#     cnt, parent = v[n]
#     if cnt == 0:
#         return
#     paths.append(parent)
#     find_path(parent)
#
# find_path(K)
# print(total_cnt)
# print(*paths[::-1])