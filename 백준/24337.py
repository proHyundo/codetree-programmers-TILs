N, a, b = map(int, input().split()) # 건물 개수, 가희가 볼 수 있는 건물 개수, 단비가 볼 수 있는 건물 개수
front = [
    h for h in range(1, a+1)
]
back = []
if b > 1:
    back = [
        h for h in range(1, b)
    ]
    front += back[::-1]

print(*front)