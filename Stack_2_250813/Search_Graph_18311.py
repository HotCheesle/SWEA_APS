graph = {}
visited = []

def DFS(vertex): 
    for v in graph[vertex]: 
        if v not in visited: 
            visited.append(v)
            DFS(v)
    return None

V, E = map(int, input().split())
for v in range(1, V+1): 
    graph[str(v)] = []
E_list = list(input().split())
for e in range(E): 
    graph[E_list[e*2]].append(E_list[e*2+1])
    graph[E_list[e*2+1]].append(E_list[e*2])

visited.append('1')
DFS('1')

print(f'#1 {"-".join(visited)}')