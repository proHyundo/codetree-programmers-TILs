m, n = map(int, input().split())
grid = [
    list(input()) for _ in range(m)
]

dxs = [1,0,-1,0,-1,1,1,-1]
dys = [0,1,0,-1,1,1,-1,-1]
ans = 0

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

def check_E(x, y):
    return grid[x][y] == 'E'

for i in range(m):
    for j in range(n):
        if grid[i][j] == 'L':
            for d in range(8):
                ni, nj = i+dxs[d], j+dys[d]
                if in_range(ni, nj) and check_E(ni, nj):
                    nni, nnj = ni+dxs[d], nj+dys[d]
                    if in_range(nni, nnj) and check_E(nni, nnj):
                        ans += 1

print(ans)