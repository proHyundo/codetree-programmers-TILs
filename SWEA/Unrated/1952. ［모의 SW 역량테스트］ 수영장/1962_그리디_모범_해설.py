# 가능한 모든 경우를 처리하는 백트래킹으로 시간제한을 통과하지 못한다면, 그리디으로 접근하는 것도 고려해볼 것.
T = int(input())
for test_case in range(1, T + 1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))

    # [2] 그리디한 방법
    D = [0] * 13
    for i in range(1, 13):
        # 가능한 4가지 방법중 i 달의 최소 비용
        mn = D[i - 1] + lst[i] * day  # 일일권
        mn = min(mn, D[i - 1] + mon)  # 월간권과 비교
        if i >= 3:
            mn = min(mn, D[i - 3] + mon3)
        if i >= 12:
            mn = min(mn, D[i - 12] + year)

        D[i] = mn
    ans = D[12]

    print(f'#{test_case} {ans}')