from collections import deque

T = 10
for t in range(1, T+1):

    l, start = map(int, input().split())
    lst = list(map(int, input().split()))
    adj = [[] for _ in range(101)]
    for i in range(0, l-1, 2):
        adj[lst[i]].append(lst[i+1])

    ans = 0


    def bfs(s):
        global ans
        q = deque()
        visited = [0] * 101

        q.append(s)
        visited[s] = 1

        while q:
            current_node = q.popleft()

            # 올바르지 않은 정답 처리
            # if visited[current_node] >= visited[ans]:
            #     ans = max(ans, current_node)

            # 정답 처리
            # 더 깊은 depth 이면 ans 를 현재 노드 번호로 갱신하고, 동일한 depth 라면 현재 노드 번호가 더 클 때 만 정답 갱신
            if visited[current_node] > visited[ans] or (visited[ans] == visited[current_node] and ans < current_node):
                ans = current_node

            for next_node in adj[current_node]:
                if visited[next_node] == 0:
                    q.append(next_node)
                    visited[next_node] = visited[current_node] + 1


    bfs(start)
    print(f'#{t}', ans)
