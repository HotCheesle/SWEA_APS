from collections import deque

def BFS(st, goal): 
    queue = deque([[st, 0]])
    visited = [st]
    while len(queue) != 0: 
        vertex = queue.popleft()
        for v in graph[vertex[0]]: 
            if v == goal: 
                return vertex[1]+1
            if v not in visited: 
                queue.append([v, vertex[1]+1])
                visited.append(v)
    return 0

T = int(input())
for tc in range(1, T+1): 
    graph = {}
    V, E = map(int, input().split())
    for i in range(1, V+1): 
        graph[i] = []
    for _ in range(E): 
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    start, goal = map(int, input().split())
    print(f'#{tc} {BFS(start, goal)}')
