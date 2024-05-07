N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
checked = [False] * 10001
ans = []

def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return

    for num in nums:
        if not checked[num+1]:
            checked[num+1] = True
            dfs(n+1, lst+[num])
            checked[num+1] = False

dfs(0, [])
for ele in ans:
    print(*ele)
