T = int(input())
for tc in range(1, T+1): 
    N, M = map(int, input().split())
    rocks = list(map(int, input().split()))
    for _ in range(M): 
        idx, cnt = map(int, input().split())
        idx -= 1
        for ofs in range(1, cnt+1): 
            if idx+ofs >= N or idx-ofs < 0: 
                break
            if rocks[idx+ofs] == rocks[idx-ofs]: 
                rocks[idx+ofs] ^= 1
                rocks[idx-ofs] ^= 1
    
    print(f'#{tc} {" ".join(map(str, rocks))}')