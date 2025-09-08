from collections import deque

def connected(pipe, row, col): 
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    disconnect = [[0, 3, 4, 7], [0, 2, 4, 5], [0, 3, 5, 6], [0, 2, 6, 7]]
    connect = []
    if pipe == 1: 
        for i in range(4): 
            nrow, ncol = row+dr[i], col+dc[i]
            if 0 <= nrow < N and 0 <= ncol < M and tunel[nrow][ncol] not in disconnect[i]: 
                connect.append((nrow, ncol))
    elif pipe == 2: 
        for i in range(0, 4, 2): 
            nrow, ncol = row+dr[i], col+dc[i]
            if 0 <= nrow < N and 0 <= ncol < M and tunel[nrow][ncol] not in disconnect[i]: 
                connect.append((nrow, ncol))
    elif pipe == 3: 
        for i in range(1, 4, 2): 
            nrow, ncol = row+dr[i], col+dc[i]
            if 0 <= nrow < N and 0 <= ncol < M and tunel[nrow][ncol] not in disconnect[i]: 
                connect.append((nrow, ncol))
    elif pipe == 4: 
        for i in range(2): 
            nrow, ncol = row+dr[i], col+dc[i]
            if 0 <= nrow < N and 0 <= ncol < M and tunel[nrow][ncol] not in disconnect[i]: 
                connect.append((nrow, ncol))
    elif pipe == 5: 
        for i in range(1, 3): 
            nrow, ncol = row+dr[i], col+dc[i]
            if 0 <= nrow < N and 0 <= ncol < M and tunel[nrow][ncol] not in disconnect[i]: 
                connect.append((nrow, ncol))
    elif pipe == 6: 
        for i in range(2, 4): 
            nrow, ncol = row+dr[i], col+dc[i]
            if 0 <= nrow < N and 0 <= ncol < M and tunel[nrow][ncol] not in disconnect[i]: 
                connect.append((nrow, ncol))
    elif pipe == 7: 
        for i in range(-1, 1): 
            nrow, ncol = row+dr[i], col+dc[i]
            if 0 <= nrow < N and 0 <= ncol < M and tunel[nrow][ncol] not in disconnect[i]: 
                connect.append((nrow, ncol))
    return connect


def BFS(srow, scol): 
    queue = deque([(srow, scol, 0)])
    visited = set()
    visited.add((srow, scol))
    while queue: 
        now = queue.popleft()
        if now[2] == L-1: 
            continue
        connect = connected(tunel[now[0]][now[1]], now[0], now[1])
        for con in connect: 
            if con not in visited: 
                visited.add(con)
                queue.append((con[0], con[1], now[2]+1))
    return len(visited)

T = int(input())
for tc in range(1, T+1): 
    N, M, R, C, L = map(int, input().split())
    tunel = list(list(map(int, input().split())) for _ in range(N))
    cnt = BFS(R, C)
    print(f'#{tc} {cnt}')