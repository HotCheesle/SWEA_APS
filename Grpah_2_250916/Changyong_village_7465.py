T = int(input())
for tc in range(1, T+1): 
    N, M = map(int, input().split())
    N += 1
    groups = list(i for i in range(N))
    par_list = set(i for i in range(1, N))
    for _ in range(M): 
        st, ed = map(int, input().split())
        x, y = groups[st], groups[ed]
        if x == y: continue
        for i in range(N): 
            if groups[i] == y: 
                groups[i] = x
        par_list.remove(y)
    print(f'#{tc} {len(par_list)}')