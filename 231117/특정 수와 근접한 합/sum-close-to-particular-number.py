import sys
n, s = map(int, input().split())
_list = list(map(int, input().split()))

_sum = sum(_list)
ans = sys.maxsize

for i in range(n-1):
    for j in range(i+1, n): 
        ans = min(ans, abs(s - (_sum - _list[i] - _list[j])))

print(abs(ans))