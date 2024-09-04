N = int(input())
requests = list(map(int, input().split()))

sum_cost, max_val = 0, 0
for r in requests:
    sum_cost += r
    max_val = max(max_val, r)

budget = int(input())

if sum_cost <= budget:  # 모든 요청이 배정될 수 있는 경우
    print(max_val)
else:   # 정수 상한액
    start = 1
    tail = max_val
    answer = start

    while start <= tail:
        pivot = (start + tail) // 2 # 125
        sm = 0
        for request in requests:
            sm += request if request <= pivot else pivot

        if sm > budget:
            tail = pivot - 1
        else:
            answer = max(answer, pivot)
            start = pivot + 1

    print(answer)