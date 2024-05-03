for _ in range(10):
    test_case = int(input())
    arr = [
        list(map(int, input().split())) for _ in range(100)
    ]

    row_max = col_max = 0
    s3 = s4 = 0

    for i in range(100):
        row_sum = col_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]

        s3 += arr[i][i]
        s4 += arr[i][100-i-1]

        row_max = max(row_sum, row_max)
        col_max = max(col_sum, col_max)

    x_max = max(s3, s4)

    print(f'#{test_case}', max(row_max, col_max, x_max))
