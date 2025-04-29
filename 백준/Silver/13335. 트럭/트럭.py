from collections import deque
n, w, L = map(int, input().split())

# n대의 트럭 지나가야 함
# w대의 트럭까지 동시 가
# L최대하중을 넘어가지 않아야 함

trucks = list(map(int, input().split()))
remain = deque(trucks)
bridge = deque()
currentWeight = 0
time = 0

while remain or bridge:

    time += 1


    # 남은 거리 1씩 감소
    bridge = deque([(w, l - 1) for w, l in bridge])

    # 다리위에 트럭이 존재하고, 가장 앞 트럭이 내려야 하는 위치라면 : 다리 위 트럭 시간 줄이고, 다리에서 내리기
    if bridge and bridge[0][1] == 0:
        weight, _ = bridge.popleft()
        currentWeight -= weight

    # 다음 트럭 올릴 수 있는지 확인
    if remain and currentWeight + remain[0] <= L and len(bridge) < w:
        weight = remain.popleft()
        bridge.append((weight, w))
        currentWeight += weight

print(time)
