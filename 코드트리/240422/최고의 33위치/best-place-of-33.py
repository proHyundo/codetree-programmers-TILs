n = int(input())
board = [
    list(map(int, input().split())) for _ in range(n)
]

answer = 0

def get_coins(i, j):
    count = 0
    for x in range(i, i+3):
        for y in range(j, j+3):

            count += board[x][y]
    return count

for i in range(n-2):
    for j in range(n-2):

        answer = max(answer, get_coins(i, j))

print(answer)