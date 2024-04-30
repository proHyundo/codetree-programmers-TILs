from itertools import permutations
N, M = map(int, input().split())
nums = [x for x in range(1, N+1)]
ans = list(permutations(nums, M))
for ele in ans:
    print(*ele)