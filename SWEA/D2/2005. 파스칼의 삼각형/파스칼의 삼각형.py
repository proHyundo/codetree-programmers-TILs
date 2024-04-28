T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    pascal = [
        [1] * N for _ in range(N)
    ]
    
    
    for i in range(2, N):
        for j in range(1, i):
            pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
    
    
    print(f'#{test_case}')
    
    for i in range(N):
        for j in range(i+1):
            print(pascal[i][j], end=' ')
        print()