graph = {}
visited = []

def DFS(vertex): 
    for v in graph[vertex]: 
        if v == '99': 
            return True
        if v not in visited: 
            visited.append(v)
            if DFS(v): 
                return True
    return False


for tc in range(1, 11): 
    _, E = map(int, input().split())
    E_list = list(input().split())
    graph.clear()
    visited.clear()
    for v in range(100): 
        graph[str(v)] = []
    for e in range(E): 
        graph[E_list[e*2]].append(E_list[e*2+1])
    visited.append('0')
    if DFS('0'): 
        print(f'#{tc} 1')
    else: 
        print(f'#{tc} 0')