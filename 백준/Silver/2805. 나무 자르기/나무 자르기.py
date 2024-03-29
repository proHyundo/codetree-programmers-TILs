N, M = map(int, input().split())
_list = list(map(int, input().split()))

start = 0
end = max(_list) - 1
ans = 0

while start <= end:
    sum = 0
    mid = (start + end) // 2

    for i in _list:
        sum += (i - mid) if (i - mid) > 0 else 0

    if sum < M:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1
print(ans)
