T = int(input())
for tc in range(1, T+1): 
    N, B = map(int, input().split())
    tall = list(map(int, input().split()))
    min_dif = 10**9
    for bits in range(1, 2**N): 
        tot = 0
        for pow in range(N): 
            if bits & 2**pow: 
                tot += tall[pow]
        dif = tot - B
        if dif >= 0: 
            min_dif = min(min_dif, dif)
    print(f'#{tc} {min_dif}')