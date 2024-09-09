import sys

N = int(input())
m_dan, m_zi, m_tan, m_be = list(map(int, input().split()))
lst = [
    list(map(int, input().split())) for _ in range(N)
]
min_cost = sys.maxsize
answer = []

def dfs(n, dan, zi, tan, be, cost, matrix):
    global answer, min_cost
    if n == N:
        if dan >= m_dan and zi >= m_zi and tan >= m_tan and be >= m_be:
            if cost < min_cost:
                # print(matrix, cost)
                answer = [matrix]
                min_cost = cost
            elif cost == min_cost:
                answer.append(matrix)
        return

    dfs(n+1, dan + lst[n][0], zi + lst[n][1], tan + lst[n][2], be + lst[n][3], cost + lst[n][4], matrix + [n+1])
    dfs(n+1, dan, zi, tan, be, cost, matrix)

dfs(0, 0, 0, 0, 0, 0, [])

if not answer:
    print(-1)
else:
    print(min_cost)
    answer.sort()
    print(*answer[0])