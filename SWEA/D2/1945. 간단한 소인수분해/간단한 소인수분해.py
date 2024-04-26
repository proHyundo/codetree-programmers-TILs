T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a = b = c = d = e = 0

    primes = {
        2: 0,
        3: 0,
        5: 0,
        7: 0,
        11: 0
    }

    for p in primes:
        while N % p == 0:
            primes[p] = primes[p] + 1
            N /= p

    print(f'#{test_case}', end=' ')
    for key in primes:
        print(primes[key], end=' ')
    print()
