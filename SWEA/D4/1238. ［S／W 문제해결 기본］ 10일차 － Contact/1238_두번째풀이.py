from collections import deque
T = 10

# 두 번째 풀이 - 해설 본 이후
def bfs(start):
    max_node = 0
    q = deque()
    q.append(start)

    v = [0] * 101

    while q:
        cur = q.popleft()
        for ele in adj[cur]:
            if v[ele] == 0:
                q.append(ele)
                v[ele] = v[cur] + 1
                if v[max_node] < v[ele] or (v[max_node] == v[ele] and max_node < ele):
                    max_node = ele

    return max_node

# 두 번째 풀이 - 해설 보기 전
# def bfs(start):
#     last_cnt = 0
#     q = deque()
#     q.append(start)
# 
#     v = [0] * 101
# 
#     while q:
#         cur = q.popleft()
#         for ele in adj[cur]:
#             if v[ele] == 0:
#                 q.append(ele)
#                 v[ele] = v[cur] + 1
#         last_cnt = v[cur]
# 
#     tmp = [0]
#     for i, ele in enumerate(v):
#         if ele == last_cnt:
#             tmp.append(i)
#     return max(tmp)

for t in range(1, T+1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    adj = [[] for _ in range(101)]
    for i in range(0, N, 2):
        adj[lst[i]].append(lst[i+1])

    print(f'#{t}', bfs(S))
