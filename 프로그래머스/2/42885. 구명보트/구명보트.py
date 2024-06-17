def solution(people, limit):
    sort_p = sorted(people)
    
    front = 0
    tail = len(people) - 1
    
    answer = 0

    while True:
        sm = 0

        if front > tail:
            break
        
        if front == tail:
            answer += 1
            break
        
        sm += sort_p[tail]
        tail -= 1
        
        if sm + sort_p[front] <= limit:
            front += 1
        
        answer += 1
        
    
    return answer