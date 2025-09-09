from heapq import heappush

def DFS(row, col, height, K, visited): 
    nvisit = visited.copy()
    leaf = True
    for r, c in zip(dr, dc):
        nrow, ncol = row+r, col+c
        if (0 <= nrow < N and 0 <= ncol < N 
            and mountain[nrow][ncol]-K < height
            and (nrow, ncol) not in nvisit): 
            nvisit.append((nrow, ncol))
            leaf = False
            if mountain[nrow][ncol] >= height: 
                DFS(nrow, ncol, height-1, 0, nvisit)
            else: 
                DFS(nrow, ncol, mountain[nrow][ncol], K, nvisit)
            nvisit.pop()
    if leaf: 
        heappush(max_heap, len(nvisit)*(-1))

T = int(input())
for tc in range(1, T+1): 
    N, K = map(int, input().split())
    mountain = list(list(map(int, input().split())) for _ in range(N))
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    high_list = [(0, 0, 0)]
    max_heap = []
    for r in range(N): 
        for c in range(N): 
            if high_list[0][2] < mountain[r][c]: 
                high_list.clear()
                high_list.append((r, c, mountain[r][c]))
            elif high_list[0][2] == mountain[r][c]:
                high_list.append((r, c, mountain[r][c]))
    for high in high_list: 
        DFS(high[0], high[1], high[2], K, [(high[0], high[1])])
    print(f'#{tc} {max_heap[0]*(-1)}')