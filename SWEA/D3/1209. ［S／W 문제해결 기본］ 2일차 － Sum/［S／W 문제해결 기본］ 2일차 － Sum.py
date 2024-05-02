for _ in range(10):
    test_case = int(input())
    arr = [
        list(map(int, input().split())) for _ in range(100)
    ]
    
    row_max = col_max = 0
    cols = [0] * 100
    xs = [0] * 2
    
    for i in range(100):
        row_sum = 0
        for j in range(100):
            if i == j:  # 대각선 1
                xs[0] += arr[i][j]
            if i + j == 100:  # 대각선 2
                xs[1] += arr[i][j]
            row_sum += arr[i][j]
            cols[j] += arr[i][j]
    
        row_max = max(row_sum, row_max)
    
    x_max = max(xs)
    col_max = max(cols)
    
    print(f'#{test_case}',max(row_max, col_max, x_max))
