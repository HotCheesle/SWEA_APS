from heapq import heappop, heappush

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    field = list(list(map(int, list(input()))) for _ in range(N))
    time_map = list([10**6]*N for _ in range(N))
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    pqueue = [(0, 0, 0)]
    visited = set()
    while pqueue: 
        now = heappop(pqueue)
        if (now[1], now[2]) in visited: continue
        visited.add((now[1], now[2]))
        time_map[now[1]][now[2]] = min(time_map[now[1]][now[2]], now[0])
        for r, c in zip(dr, dc): 
            nrow, ncol = now[1]+r, now[2]+c
            if 0 <= nrow < N and 0 <= ncol < N and (nrow, ncol) not in visited: 
                heappush(pqueue, (time_map[now[1]][now[2]]+field[nrow][ncol], nrow, ncol))
    print(f'#{tc} {time_map[N-1][N-1]}')