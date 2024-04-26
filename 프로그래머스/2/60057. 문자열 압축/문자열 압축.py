import sys

def solution(s):
    answer = sys.maxsize
    length = len(s)
    if length == 1:
        return 1
    
    for r in range(1, length//2+1): # 자르는 길이
        sliced = []
        compressed = ''
        for start in range(0, length, r):
            sliced.append(s[start:start+r])
        
        # 비교
        cnt = 1
        for i in range(0, len(sliced) - 1):
            cur = sliced[i]
            next = sliced[i+1]
            
            if cur == next:
                cnt += 1
            else:
                if cnt == 1:
                    compressed += cur
                else:
                    compressed += (str(cnt) + cur)
                cnt = 1
                
        if cnt > 1:
            compressed += (str(cnt) + sliced[-1])
        else:
            compressed += sliced[-1]
            
        answer = min(answer, len(compressed))
    
    return answer