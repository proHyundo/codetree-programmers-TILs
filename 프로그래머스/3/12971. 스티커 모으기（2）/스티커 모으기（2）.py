def solution(sticker):
    answer = 0
    N = len(sticker)
    if N == 1:
        return sticker[0]
    
    dp1 = [0] * (N+1)  # 첫 번째 요소 선택
    dp2 = [0] * (N+1)  # 두 번째 요소 선택

    dp1[1] = sticker[0]
    dp2[1] = 0

    for i in range(2, N+1):
        if i-2 >= 0:
            dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i-1])
            dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i-1])
        else:
            dp1[i] = max(dp1[i-1], sticker[i-1])
            dp2[i] = max(dp2[i-1], sticker[i-1])


    return max(dp1[N-1], dp2[N])