from heapq import heappush, heappop

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    height_map = list(list(map(int, input().split())) for _ in range(N))
    fuel_map = list([10**7]*N for _ in range(N))
    pqueue = [(0, 0, 0)] # (fule, row, col)
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    visited = set([])
    while pqueue: 
        check = heappop(pqueue)
        if (check[1], check[2]) in visited: continue
        visited.add((check[1], check[2]))
        if fuel_map[check[1]][check[2]] > check[0]: 
            fuel_map[check[1]][check[2]] = check[0]
        for r, c in zip(dr, dc): 
            nrow, ncol = check[1]+r, check[2]+c
            if 0 <= nrow < N and 0 <= ncol < N and (nrow, ncol) not in visited: 
                hdif = height_map[nrow][ncol] - height_map[check[1]][check[2]]
                if hdif < 0: hdif = 0
                heappush(pqueue, (fuel_map[check[1]][check[2]]+hdif+1, nrow, ncol))
    print(f'#{tc} {fuel_map[N-1][N-1]}')