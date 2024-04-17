import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    ans = 0
    total_time = 0
    
    q = []
    for index, time in enumerate(food_times):
        heapq.heappush(q, (time, index+1))
    
    length = len(q)
    
    while (q[0][0] - total_time) * length < k:
        cur_food_time = heapq.heappop(q)[0] - total_time
        
        k -= cur_food_time * length
        total_time += cur_food_time
        length -= 1
    

    q.sort(key = lambda x: x[1])
    return q[k%length][1]
        
