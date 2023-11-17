import sys
s, n = map(int, input().split())
_list = list(map(int, input().split()))

_sum = sum(_list)
diff = sys.maxsize

for i in range(s-1):
    for j in range(i+1, s): 
        diff = min(diff, _sum - _list[i] - _list[j])

print(abs(n - diff))