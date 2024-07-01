def solution(sequence):
    sequence1 = []
    sequence2 = []
    value = -1
    for s in sequence:
        sequence1.append(s * value)
        value *= -1
        sequence2.append(s * value)

    N = len(sequence)
    dp1 = [0] * N
    dp2 = [0] * N
    dp1[0] = sequence1[0]
    dp2[0] = sequence2[0]

    for i in range(1, N):
        dp1[i] = max(dp1[i-1] + sequence1[i], sequence1[i])
        dp2[i] = max(dp2[i-1] + sequence2[i], sequence2[i])


    return max(max(dp1), max(dp2))