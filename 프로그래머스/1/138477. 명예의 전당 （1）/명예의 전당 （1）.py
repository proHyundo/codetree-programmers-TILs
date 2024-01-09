def solution(k, score):
    answer = []
    prize = []
    for i, s in enumerate(score):
        prize.append(s)
        prize.sort(reverse=True)
        if len(prize) < k:
            answer.append(min(prize))
        else:
            answer.append(prize[k-1])

    
    return answer