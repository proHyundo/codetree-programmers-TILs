def solution(n):
    answer = 0
    for x in range(1, 1000001):
        if n % x == 1:
            answer = x
            break
    return answer