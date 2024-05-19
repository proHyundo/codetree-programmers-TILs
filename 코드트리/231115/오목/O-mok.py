grid = [
    list(map(int, input().split())) for _ in range(19)
]
checked = [
    [False] * 19 for _ in range(19)
]
dxs = [0,1,0,-1,-1,1,1,-1]
dys = [1,0,-1,0,1,1,-1,-1]

def in_range(i, j):
    if 0 <= i <= 18 and 0 <= j <= 18:
        return True
    else:
        return False

def check_omock(i, j, target, direction):
    global cnt    
    cnt += 1
    checked[i][j] = True
    if cnt == 5:
        return i, j

    dx, dy = direction
    nx = dx + i
    ny = dy + j
    if in_range(nx, ny) and target == grid[nx][ny] and not checked[nx][ny]:
        return check_omock(nx, ny, target, direction)
    return False

exit_flag = False
for i in range(19):
    for j in range(19):
        if grid[i][j] == 1 or grid[i][j] == 2:
            for direction in zip(dxs, dys):
                cnt = 0
                result = check_omock(i, j, grid[i][j], direction)
                if result:
                    ni, nj = result
                    ans_x = 0
                    ans_y = 0

                    if i == ni:
                        ans_x = i+1
                    else:
                        ans_x = int((i + 1 + ni + 1) / 2)

                    if j == nj:
                        ans_y = j+1
                    else:
                        ans_y = int((j + 1 + nj + 1) / 2)
                    
                    print(grid[i][j])
                    print(ans_x, ans_y)
                    exit_flag = True
                    break
    if exit_flag:
        break

if exit_flag == False:
    print(0)