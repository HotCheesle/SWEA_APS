from collections import deque

def BFS(st): 
    queue = deque([(st, 0)])
    while queue: 
        now = queue.popleft()
        for ed in range(N): 
            if st == ed: continue
            if adjacency_matrix[now[0]][ed] != 0 and dmap[st][ed] == 0: 
                dmap[st][ed] = now[1]+1
                queue.append((ed, now[1]+1))


T = int(input())
for tc in range(1, T+1): 
    input_list = list(map(int, input().split()))
    N = input_list[0]
    adjacency_matrix = [None for _ in range(N)]
    for i in range(N): 
        adjacency_matrix[i] = input_list[(i*N)+1: ((i+1)*N)+1]
    del(input_list)
    dmap = list([0]*N for _ in range(N))
    for st in range(N): 
        BFS(st)
    min_CC = 10**6
    for i in range(N): 
        CC = sum(dmap[i])
        if min_CC > CC: 
            min_CC = CC
    print(f'#{tc} {min_CC}')