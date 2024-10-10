N = int(input())
nums = [0] + [
    int(input()) for _ in range(N)
]
visited = [False] * (N+1)
answer = set()


def dfs(cur):

    global tmp_keys, tmp_values

    visited[cur] = True
    nxt = nums[cur]
    tmp_keys.add(cur)
    tmp_values.add(nxt)

    if not visited[nxt] and nxt != nums[nxt]:
        dfs(nxt)
    else:
        return

for i in range(1, N+1):
    n = nums[i]
    if not visited[n]:
        tmp_keys = set()
        tmp_values = set()
        dfs(n)
        if tmp_keys == tmp_values:
            answer = answer.union(tmp_keys)

print(len(answer))
print(*sorted(answer),sep='\n')