T = int(input())
for test_case in range(1, T+1):
    lst = [0] * 5001
    N = int(input())
    for n in range(N):
        start, end = map(int, input().split())
        for i in range(start, end+1):
            lst[i] += 1

    P = int(input())
    sols = []
    for _ in range(P):
        sols.append(lst[int(input())])

    print(f'#{test_case}', *sols)