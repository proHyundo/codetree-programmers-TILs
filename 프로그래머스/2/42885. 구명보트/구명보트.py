def solution(people, limit):
    sort_p = sorted(people)
    answer = 0
    
    front = 0
    tail = len(people) - 1
    
    while front <= tail:
        
        if front == tail:
            answer += 1
            break

        if sort_p[tail] + sort_p[front] <= limit:
            front += 1
        
        tail -= 1
        answer += 1
        
    return answer