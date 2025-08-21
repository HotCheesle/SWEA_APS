node = {}
arr = []
for i in range(2):
    arr.append(list(input()))

for i in range(2):
    for j in range(3):
        node[(i,j,'W')] = []
        node[(i,j,'L')] = []

print(node)
for i in range(2):
    for j in range(3):
        if arr[i][j] == 'W':
            node[(i,j,'W')].append((i,j,'W'))
        if arr[i][j] == 'L':
            node[(i,j,'L')].append((i,j,'L'))

visited = [[False] * 3 for _ in range(2)]

from collections import deque

def bfs(start):
    stack = deque([(start)])
    while stack:
        x,y,i = stack.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            for x1,y1,state in sorted(node[(x,y,i)], reverse= True):
                stack.append((x1,y1,state))
                if state == 'W':
                    return x1,y1

print(bfs((1,1,'L')))