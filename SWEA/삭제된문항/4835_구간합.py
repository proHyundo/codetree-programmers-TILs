import sys

N, M = map(int, input().split())
arr = list(map(int, input().split()))
minVal = sys.maxsize
maxVal = -sys.maxsize

for i in range(0, N-M+1):
    sumVal = sum(arr[i:i+M])
    minVal = min(minVal, sumVal)
    maxVal = max(maxVal, sumVal)

print(maxVal - minVal)
