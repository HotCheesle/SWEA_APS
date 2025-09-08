T = int(input())
for tc in range(1, T+1): 
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    for bits in range(1, 2**N):
        tot = 0
        for pow in range(N): 
            if bits & 1<<pow: 
                tot += arr[pow]
        if tot == K: 
            cnt += 1
    print(f'#{tc} {cnt}')
