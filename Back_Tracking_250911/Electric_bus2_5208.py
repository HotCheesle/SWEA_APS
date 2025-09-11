def drive(bus, cnt, bettary): 
    global min_cnt
    for dis in range(1, bettary+1): 
        if bus+dis == N: 
            min_cnt = min(min_cnt, cnt)
            return
        if bettary-dis < route[bus+dis] and cnt+1 < min_cnt: 
            drive(bus+dis, cnt+1, route[bus+dis])

T = int(input())
for tc in range(1, T+1): 
    route = list(map(int, input().split()))
    N = route[0]
    min_cnt = 100
    drive(1, 0, route[1])
    print(f'#{tc} {min_cnt}')