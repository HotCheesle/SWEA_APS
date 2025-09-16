from heapq import heappush, heappop

def find_set(x): 
    par = tree_set.get(x)
    if par is None: 
        for key, val in tree_set.items(): 
            if x in val: 
                par = key
                break
    else: 
        par = x
    return par

def union(x, y): 
    tree_set[x].update(tree_set[y])
    tree_set.pop(y)

T = int(input())
for tc in range(1, T+1): 
    V, E = map(int, input().split())
    graph = list([0]*(V+1) for _ in range(V+1)) # 인접 행렬
    edge_list = [] # 간선 리스트
    for _ in range(E): 
        st, ed, w = map(int, input().split())
        graph[st][ed] = w
        graph[ed][st] = w
        edge_list.append((w, st, ed))
    
    # Prim 알고리즘
    # tree_set, edge_heap = set([0]), []
    # tot_weight, st= 0, 0
    # while len(tree_set) != V+1: 
    #     for ed in range(V+1): 
    #         if ed not in tree_set and graph[st][ed] != 0: 
    #             heappush(edge_heap, (graph[st][ed], st, ed))
    #     edge = heappop(edge_heap)
    #     while edge[2] in tree_set: 
    #         edge = heappop(edge_heap)
    #     st = edge[2]
    #     tot_weight += edge[0]
    #     tree_set.add(edge[2])

    # Kruskal 알고리즘
    edge_list.sort(key=lambda e: e[0])
    tot_weight, edge_cnt = 0, 0
    tree_set = {i: {i} for i in range(V+1)}
    for edge in edge_list: 
        x, y = find_set(edge[1]), find_set(edge[2])
        if x == y: continue
        union(x, y)
        tot_weight += edge[0]
        edge_cnt += 1
        if edge_cnt == V: break

    print(f'#{tc} {tot_weight}')
