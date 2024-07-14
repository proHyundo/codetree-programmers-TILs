# from collections import deque
# def solution(tickets):
#     answer = []
#     adj = dict()
#     for start, end in tickets:
#         if start in adj:
#             adj[start] = adj.get(start) + [end]
#         else:
#             adj[start] = [end]
#
#     for key, val in adj.items():
#         adj[key] = sorted(val)
#     print(adj)
#     def bfs(ICN):
#         q = deque()
#         q.append(ICN)
#
#         while q:
#             curr = q.popleft()
#             answer.append(curr)
#             if curr in adj:  # 꺼낸 공항이 인접리스트에 이어진 공항이 존재한다면
#                 lst = adj.get(curr)
#
#                 if len(lst) == 1: # 이어진 공항이 1개라면
#                     q.append(adj.pop(curr)[0]) # 공항 pop
#
#                 else: # 이어진 공항이 여러개 라면
#                     for airport in lst: # 각 공항을 순회하면서 이어진 공항이 있는 공항을 선택
#                         if airport in adj:
#                             q.append(airport)
#                             lst.remove(airport)
#                             adj[curr] = lst
#                             break
#
#     bfs("ICN")
#     return answer

# ----------------------------------------------------------------------------------------------------------------------
from collections import defaultdict

# 풀이 링크 : https://velog.io/@ledcost/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-43164-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C-level-3-BFSDFS
def solution(tickets):
    t_dict = defaultdict(list)

    # key: 출발지, value: 목적지인 딕셔너리 만듦
    for s, e in tickets:
        t_dict[s].append(e)

    # 목적지 기준 내림차순 정렬(맨 오른쪽걸 pop해서 쓸거임. 알파벳 순서 상 가장 앞선 것)
    for t_key in t_dict.keys():
        t_dict[t_key].sort(reverse=True)

    answer = []
    path = ["ICN"]

    # DFS를 실행함. 처음에는 맨 마지막 공항까지 쭉쭉 나아감.
    # 어느 순간 다른 공항으로 가는 티켓도 없고, 또는 그런 티켓을 다 소진한
    # 어떤 공항에 도착한다면 그 곳이 맨 마지막에 도달하게 될 공항임.
    # 이제 path에서 pop해서 하나씩 answer에 넣어줌으로써 path를 역방향으로
    # 거슬러 올라갈거임. 다만 맨 마지막 공항에 처음으로 도착했을 때의 path
    # 가 모든 간선을 다 사용하지 않은 path일 수도 있음. 그러므로, 한 칸씩
    # 내려가면서 그 공항과 연결된 인접 공항들을 싹 다 돌아주면 됨.
    # 이렇게 ICN까지 쭉 실행해주면 path는 비게 되고 answer에는 역방향의 정답
    # 루트가 담겨있게 됨.
    while path:
        now = path[-1]

        if now not in t_dict or len(t_dict[now]) == 0:
            answer.append(path.pop())
        else:
            path.append(t_dict[now].pop())

    return answer[::-1]

print(solution([["ICN", "BBB"], ["BBB", "ICN"], ["ICN", "AAA"]]))

# 풀이 링크 : https://1minute-before6pm.tistory.com/76