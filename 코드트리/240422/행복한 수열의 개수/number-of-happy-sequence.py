n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def find_seq(target):
    count, max_count = 1, 1
    for i in range(0, n-1):
        if target[i] == target[i+1]:
            count += 1
            if count >= m:
                return True
        else:
            count = 1
        max_count = max(count, max_count)

    return count >= m


for i in range(n): # 행 가져오기
    if find_seq(board[i]):
        answer += 1

for j in range(n): # 열 가져오기
    if find_seq([row[j] for row in board]):
        answer += 1

print(answer)