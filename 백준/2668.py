N = int(input())
nums = [0] + [
    int(input()) for _ in range(N)
]
visited = [False] * (N+1)
answer = set()


def dfs(start, target):
    nxt = nums[start]
    if not visited[nxt]:
        visited[nxt] = True
        dfs(nxt, target)
        visited[nxt] = False
    if nxt == target:
        answer.add(target)

for i in range(1, N+1):
    visited[i] = True
    dfs(i, i)
    visited[i] = False

print(len(answer))
print(*sorted(answer), sep='\n')