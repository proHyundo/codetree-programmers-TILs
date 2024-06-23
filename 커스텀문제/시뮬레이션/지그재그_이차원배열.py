# 문제 출처 : https://blog.naver.com/azure0777/220276103335

N = int(input())
cx, cy = 0, 0
ex, ey = N - 1, N - 1

draw = [[0] * N for _ in range(N)]
draw[0][0] = 1
flag = True
cnt = 2


def go_right(x, y):
    global cnt
    draw[x][y + 1] = cnt
    cnt += 1
    return x, y + 1


def go_down(x, y):
    global cnt
    draw[x + 1][y] = cnt
    cnt += 1
    return x + 1, y


def go_up_right(x, y):
    global cnt
    for i in range(1, abs(x - y) + 1):
        draw[x - i][y + i] = cnt
        cnt += 1
    return y, x


def go_down_left(x, y):
    global cnt
    for i in range(1, abs(x - y) + 1):
        draw[x + i][y - i] = cnt
        cnt += 1
    return y, x


for _ in range(N-1):
    if flag:
        cx, cy = go_right(cx, cy)
        cx, cy = go_down_left(cx, cy)
    else:
        cx, cy = go_down(cx, cy)
        cx, cy = go_up_right(cx, cy)

    flag = not flag


# N이 짝수라서 상부 함수가 (N-1, 0)에서 끝나는 경우
if N % 2 == 0:
    flag = True
else:
    flag = False


while (cx, cy) != (N-1, N-1):
    # 현재 위치가 오른쪽 한 칸 전진만을 남겨 놓고 있는 경우
    if (cx, cy) == (N - 1, N - 2):
        go_right(cx, cy)
        break

    # N이 짝수라서 상부 함수가 (N-1, 0)에서 끝나는 경우
    if flag:
        cx, cy = go_right(cx, cy)
        cx, cy = go_up_right(cx, cy)
    else:
        cx, cy = go_down(cx, cy)
        cx, cy = go_down_left(cx, cy)

    flag = not flag

for row in draw:
    print(*row, sep='\t')
