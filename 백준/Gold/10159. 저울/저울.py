N = int(input())
M = int(input())

def dfs(node, graph):
    res = 1
    for nxt in graph[node]:
        if not is_visited[nxt]:
            is_visited[nxt] = True
            res += dfs(nxt, graph)
    return res


forward_graph = {i: [] for i in range(1, N+1)}  # 나보다 가벼운 물건들
reverse_graph = {i: [] for i in range(1, N+1)}  # 나보다 무거운 물건들

for _ in range(M):
    heavy, light = map(int, input().split())
    forward_graph[heavy].append(light)
    reverse_graph[light].append(heavy)

for i in range(1, N+1):
    is_visited = [False] * (N + 1)
    is_visited[i] = True
    lighter = dfs(i, forward_graph) - 1

    is_visited = [False] * (N + 1)
    is_visited[i] = True
    heavier = dfs(i, reverse_graph) - 1

    print(N - (lighter + heavier + 1))
