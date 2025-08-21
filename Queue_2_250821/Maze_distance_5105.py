from collections import deque

def BFS(st, N): 
    queue = deque([st])
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    while len(queue) != 0: 
        point = queue.popleft()
        for r, c in zip(dr, dc): 
            if 0 <= point[0]+r < N and 0 <= point[1]+c < N: 
                if maze[point[0]+r][point[1]+c] == 3: 
                    return maze[point[0]][point[1]] - 10
                if maze[point[0]+r][point[1]+c] == 0:
                    maze[point[0]+r][point[1]+c] = maze[point[0]][point[1]] + 1
                    queue.append([point[0]+r, point[1]+c])
    return 0

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    maze = list(list(map(int, input())) for _ in range(N))

    for i in range(N): 
        for j in range(N): 
            if maze[i][j] == 2: 
                maze[i][j] = 10
                start = [i, j]
                break
    print(f'#{tc} {BFS(start, N)}')