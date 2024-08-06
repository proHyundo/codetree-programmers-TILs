from collections import deque

N, M = map(int, input().split())    # N : 가수 수, M : PD 수
indegree = [0] * (N + 1)            # 가수 수 만큼 준비, 초기 진입 차수 0
adj = [[] for _ in range(N + 1)]    # 그래프를 인접리스트로 표현
for _ in range(M):                  # PD 수 만큼 순회
    lst = list(map(int, input().split()))
    for i in range(1, lst[0]):      # len - 1 까지 index 순회
        a, b = lst[i], lst[i+1]
        adj[a].append(b)            # a -> b
        indegree[b] += 1            # b로 진입하는 a가 있으니 += 1


def topology_sort():
    result = []
    q = deque()

    for index in range(1, N + 1):
        if indegree[index] == 0:
            q.append(index)

    while q:
        cur = q.popleft()
        result.append(cur)

        for node in adj[cur]:
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)

    if len(result) != N:
        print(0)
    else:
        for ele in result:
            print(ele)


topology_sort()