# 문제 이름: [문제 이름 삽입]
# 해결 날짜: [YY-MM-DD 형식으로 날짜 삽입]
# 소요 시간: [문제를 해결하는데 걸린 시간 삽입, 예: 45분]
# 시간 복잡도: [해결책의 시간 복잡도 삽입, 예: O(n), O(n^2) 등]
# 난이도: [난이도 수준 삽입, 예: 상, 중, 하]
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: [문제 해결에 접근한 방식을 간략히 설명. 여기에는 사용된 알고리즘, 데이터 구조 및 주목할 만한 최적화가 포함될 수 있음.]
# 코멘트: [문제나 해결책과 관련된 추가 코멘트나 비고 사항.]


def solution():
    N = int(input())
    K = int(input())
    head, tail = (1, 1), (1, 1)
    direction = 0
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    paths = [(1, 1)]
    eat_cnt = 0
    apples = {tuple(map(int, input().split())) for _ in range(K)}
    order_cnt = int(input())
    orders = [tuple(input().split()) for _ in range(order_cnt)]
    total = int(orders[-1][0])
    times = [False] * (total+N)
    for o in orders:
        time, dir = o
        times[int(time)] = dir

    def not_body(nx, ny):
        body = paths[-2:-2-eat_cnt:-1]
        # print('body', body)
        return True if (nx, ny) not in body else False

    time = 1
    while True:
        nx = head[0] + dxs[direction]
        ny = head[1] + dys[direction]
        if 1 <= nx <= N and 1 <= ny <= N and not_body(nx, ny):
            if (nx, ny) in apples:
                apples.remove((nx, ny))
                eat_cnt += 1
            head = (nx, ny)
            paths.append((nx, ny))

        else:
            # print('paths', paths)
            return time

        if times[time]:
            direction = (direction + 1) % 4 if times[time] == 'D' else (direction + 3) % 4

        time += 1

print(solution())
