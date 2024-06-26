N, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()

dp2 = [1] + [0] * K
for i in range(N):
    for j in range(lst[i], K+1):
        dp2[j] += dp2[j - lst[i]]

print(dp2[-1])