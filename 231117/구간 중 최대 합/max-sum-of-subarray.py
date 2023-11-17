n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_val = 0

for i in range(n-k+2):
    max_val = max(max_val, sum(arr[i:i+3:]))

print(max_val)