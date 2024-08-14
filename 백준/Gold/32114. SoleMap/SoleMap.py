import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 도시의 수, 차량 정보

# 유동 차량 초기 세팅, 도로 세팅
cars = [0] * (N+1)
loads = [0] + list(map(int, input().split()))

# 유동 차량 세팅
# for _ in range(M):
#     u, v, x = map(int, input().split())
#     for j in range(u, v):
#         cars[j] += x

# 유동 차량 세팅 : Difference Array Technique 참고 링크 : https://jypark1111.tistory.com/m/201
for _ in range(M):
    u, v, x = map(int, input().split())
    cars[u] += x
    cars[v] -= x

for i in range(1, N):
    cars[i] += cars[i-1]


def find_min_cost(l, c):
    common = c // l # 공통
    diff = c - (c // l * l) # 차이나는 값
    return ((common+1) ** 2 * diff) + (common ** 2 * (l-diff))


for i in range(1, N):
    load, car = loads[i], cars[i]
    if load == 1:
        sys.stdout.write(str(car**2) + '\n')
    elif load >= car:
        sys.stdout.write(str(car) + '\n')
    else:
        sys.stdout.write(str(find_min_cost(load, car)) + '\n')
