from collections import deque

def BFS(st): 
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    queue = deque([st])
    while len(queue) != 0: 
        point = queue.popleft()
        for r, c in zip(dr, dc): 
            if 0 <= point[0]+r < 16 and 0 <= point[1]+c < 16: 
                if maze[point[0]+r][point[1]+c] == 0:
                    maze[point[0]+r][point[1]+c] = 2
                    queue.append([point[0]+r, point[1]+c])
                elif maze[point[0]+r][point[1]+c] == 3:
                    return True
    return False


for tc in range(1, 11): 
    _ = input()
    maze = list(list(map(int, input())) for _ in range(16))

    for i in range(16): 
        for j in range(16): 
            if maze[i][j] == 2: 
                start = [i, j]
                break

    if BFS(start): 
        print(f'#{tc} 1')
    else: 
        print(f'#{tc} 0')