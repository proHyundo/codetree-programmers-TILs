N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
checked = [False] * 10001
ans = []


def dfs(n, start_index, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(start_index, N):
        if not checked[nums[i]+1]:
            checked[nums[i]+1] = True
            dfs(n+1, i+1, lst + [nums[i]])
            checked[nums[i]+1] = False


dfs(0, 0, [])
for ele in ans:
    print(*ele)
