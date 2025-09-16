from heapq import heappush, heappop
from math import sqrt
def dist(p1, p2): 
    x = abs(p1[0]-p2[0])
    y = abs(p1[1]-p2[1])
    return sqrt(x**2+y**2)

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    E = float(input())

    adjacency_matrix = list([0.0]*N for _ in range(N))
    for st in range(N): 
        for ed in range(st+1, N): 
            weight = dist((island_x[st], island_y[st]) 
                      , (island_x[ed], island_y[ed]))**2 * E
            adjacency_matrix[st][ed] = weight
            adjacency_matrix[ed][st] = weight
    
    pqueue = []
    vertex_set = set([0])
    tot_cost = 0.0
    for ed in range(1, N): 
        heappush(pqueue, (adjacency_matrix[0][ed], 0, ed))
    while pqueue: 
        if len(vertex_set) == N: break
        cur = heappop(pqueue)
        if cur[1] in vertex_set and cur[2] in vertex_set: continue
        vertex_set.add(cur[2])
        tot_cost += cur[0]
        for ed in range(N): 
            if cur[2] == ed: continue
            heappush(pqueue, (adjacency_matrix[cur[2]][ed], cur[2], ed))
    print(f'#{tc} {tot_cost:.0f}')