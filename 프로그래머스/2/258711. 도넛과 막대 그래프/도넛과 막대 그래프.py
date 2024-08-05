def solution(edges):
    answer = [0, 0, 0, 0]
    adj = dict()    # "노드번호": [진출, 진입]
    for a, b in edges:
        if a not in adj:
            adj[a] = [0, 0]
        if b not in adj:
            adj[b] = [0, 0]
        adj.get(a)[0] += 1
        adj.get(b)[1] += 1

    for key, lst in adj.items():
        if lst[0] >= 2 and lst[1] == 0: # 시작 노드
            answer[0] = key
        elif lst[0] == 2 and lst[1] >= 2: # 8자 그래프
            answer[3] += 1
        elif lst[0] == 0 and lst[1] >= 1: # 직선 그래프
            answer[2] += 1

    answer[1] = adj.get(answer[0])[0] - sum(answer[2:])

    return answer