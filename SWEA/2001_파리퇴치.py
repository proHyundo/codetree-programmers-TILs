import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [
    list(map(int, input().split())) for _ in range(n)
]

ans = 0

for i in range(0, n-m+1):
    for j in range(0, n-m+1):
        count = 0
        for x in range(m):
            for y in range(m):
                count += board[i+x][j+y]
        ans = max(ans, count)

print(ans)