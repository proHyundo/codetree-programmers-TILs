import sys

input = sys.stdin.readline
N, K = map(int, input().split())
lst = list(map(int, input().split()))
robots = [False] * N

answer = 0

while True:
    answer += 1
    # 컨베이어 벨트 & 로봇 한 칸 회전
    lst = [lst[-1]] + lst[:N*2-1]
    robots = [False] + robots[:N-1]

    # 로봇 이동
    # 마지막 인덱스는 로봇 있던 없던 내림처리
    robots[N-1] = False
    for i in range(N-2, -1, -1):
        # 로봇 이동 가능한 경우, 이동 후 내구도 감소
        if robots[i] and not robots[i+1] and lst[i+1] >= 1:
            robots[i+1] = True
            robots[i] = False
            lst[i+1] -= 1

    # 첫 번째 인덱스에 로봇 올림 & 내구도 감소
    if lst[0] >= 1:
        robots[0] = True
        lst[0] -= 1

    # 내구도 확인
    if lst.count(0) >= K:
        break


print(answer)
