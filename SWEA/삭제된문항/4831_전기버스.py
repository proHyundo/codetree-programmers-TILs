# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동,
# 한 번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력.
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다.
# 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

K, N, M = map(int, input().split())
arr = list(map(int, input().split()))
lst = [False] * (N+1)
for index in arr:
    lst[index] = True
cnt = 0
cur = 0

while cur < N:
    if cur+K >= N:
        cur += K
        break
    if lst[cur+K]:
        cnt += 1
        cur += K
    else:
        find = False
        for i in range(cur+K-1, cur+1, -1):
            if lst[i]:
                cnt += 1
                cur = i
                find = True
                break
        if not find:
            break

if cur < N:
    print(0)
else:
    print(cnt)