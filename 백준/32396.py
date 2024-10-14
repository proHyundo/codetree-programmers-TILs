N, M = map(int, input().split())
arr = list(map(int, input().split())) + [0, 0]
ans = 0

print(arr)

for i in range(N-1):
    if abs(arr[i+1] - arr[i]) >= M:
        continue
    else:
        if arr[i+1] >= arr[i]:
            arr[i+1] = max(arr[i+2], arr[i]) + M
        else:
            arr[i] = max(arr[i-1], arr[i+1]) + M
        ans += 1


print(arr)
print(ans)