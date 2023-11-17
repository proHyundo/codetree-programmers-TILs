n = int(input())
grid = [
    list(map(int, input().split())) for _ in range(n)
]
ans = 0

def not_cross(i, j, k, l):
    temp_a = [(i,j), (i, j+1), (i, j+2)]
    temp_b = [(k,l), (k, l+1), (k, l+2)]
    for a in temp_a:
        if a in temp_b:
            return False
    return True

def get_coins(i, j, k, l):
    return grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[k][l] + grid[k][l+1] + grid[k][l+2]
    

for i in range(n):
    for j in range(n-2):
        for k in range(n):
            for l in range(n-2):
                if not_cross(i, j, k, l):
                    ans = max(get_coins(i, j, k, l), ans)

print(ans)