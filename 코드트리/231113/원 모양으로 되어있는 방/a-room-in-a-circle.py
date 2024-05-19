import sys
n = int(input())
rooms = [
    int(input()) for _ in range(n)
]

ans = sys.maxsize

for i in range(n):
    distance = 0
    for j in range(1, n):
        distance += rooms[(i + j) % n] * j
    ans = min(ans, distance)

print(ans)