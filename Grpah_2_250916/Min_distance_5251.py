from heapq import heappop, heappush

T = int(input())
for tc in range(1, T+1): 
    V, E = map(int, input().split())
    V += 1
    graph = list([0]*V for _ in range(V))
    confirm = set()
    dmap = [10**6]*V
    for _ in range(E): 
        st, ed, w = map(int, input().split())
        graph[st][ed] = w
    pqueue = [(0, 0)]
    while pqueue: 
        cur = heappop(pqueue)
        if cur[1] in confirm: continue
        if dmap[cur[1]] > cur[0]: 
            dmap[cur[1]] = cur[0]
        confirm.add(cur[1])
        for ed in range(V): 
            if ed not in confirm and graph[cur[1]][ed] != 0: 
                heappush(pqueue, (dmap[cur[1]]+graph[cur[1]][ed], ed))
    print(f'#{tc} {dmap[V-1]}')