from itertools import permutations

def isNotPrime(num):
    if num < 2:
        return True
    
    for i in range(2, num):
            if num % i == 0:
                return True
    
    return False

def solution(numbers):
    _set = set()
    for i in range(1, len(numbers)+1):
        for cou in permutations(numbers, i):
            _set.add(int(''.join(cou)))
    
    ans = len(_set)
    for num in _set:
        if isNotPrime(num):
            ans -= 1
            continue
            
    return ans