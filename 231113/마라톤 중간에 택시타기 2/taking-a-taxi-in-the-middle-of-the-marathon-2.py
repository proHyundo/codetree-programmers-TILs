import sys
n = int(input())
courses = [
    tuple(map(int, input().split())) for _ in range(n)
]

ans = sys.maxsize

for jump_i in range(1, n-1):
    temp_courses = courses[0:jump_i:1] + courses[jump_i+1::]
    length = 0
    for i in range(n-2):
        length += abs(temp_courses[i][0] - temp_courses[i+1][0]) + abs(temp_courses[i][1] - temp_courses[i+1][1])
    
    ans = min(ans, length)

print(ans)