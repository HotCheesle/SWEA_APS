def DFS(row, col): 
    for r, c in zip(dr, dc): 
        if 0 <= row+r < N and 0 <= col+c < N: 
            if maze[row+r][col+c] == '3': 
                return True
            elif maze[row+r][col+c] == '0': 
                maze[row][col] = '2'
                if DFS(row+r, col+c): 
                    return True
    return False

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1): 
    N = int(input().strip())
    maze = list(list(input().strip()) for _ in range(N))
    is_find = None
    for row in range(N): 
        for col in range(N): 
            if maze[row][col] == '2': 
                is_find = DFS(row, col)
                break
        if is_find != None: 
            break
    if is_find: 
        print(f'#{tc} 1')
    else: 
        print(f'#{tc} 0')