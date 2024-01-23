def solution(brown, yellow):
    tup = tuple()
    by = brown + yellow
    for i in range(1, by+1):
        if (by % i == 0) and (i >= by // i) and (yellow == (i-2)*(by//i-2)):
            tup = ((i,by//i))
            break
    
    
    return [tup[0], tup[1]]