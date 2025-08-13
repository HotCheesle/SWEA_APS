graph = {}
visited = []

def DFS(vertex, goal): 
    for v in graph[vertex]: 
        if v not in visited: 
            if v == goal: 
                return True
            visited.append(v)
            if DFS(v, goal): 
                return True
    return False

T = int(input())
for tc in range(1, T+1): 
    graph.clear()
    visited.clear()
    V, E = map(int, input().split())
    for v in range(1, V+1): 
        graph[str(v)] = []
    for e in range(E): 
        s, g = input().split()
        graph[s].append(g)
    
    start, goal = input().split()

    visited.append(start)
    if DFS(start, goal): 
        print(f'#{tc} 1')
    else: 
        print(f'#{tc} 0')