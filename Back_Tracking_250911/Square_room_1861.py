def DFS_up(row, col, length, tg):
    visited[row][col] = True
    for r, c in zip(dr, dc): 
        nrow, ncol = row+r, col+c
        if 0 <= nrow < N and 0 <= ncol < N and rooms[nrow][ncol] == tg: 
            length = DFS_up(nrow, ncol, length+1, tg+1)
            return length
    return length

def DFS_down(row, col, length, tg):
    global st
    visited[row][col] = True
    for r, c in zip(dr, dc): 
        nrow, ncol = row+r, col+c
        if 0 <= nrow < N and 0 <= ncol < N and rooms[nrow][ncol] == tg: 
            length = DFS_down(nrow, ncol, length+1, tg-1)
            return length
    st = rooms[row][col]
    return length

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    rooms = list(list(map(int, input().split()))for _ in range(N))
    visited = list([False]*N for _ in range(N))
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    max_len = 1
    max_rooms = []
    for row in range(N): 
        for col in range(N): 
            st = rooms[row][col]
            if rooms[row][col] < N**2 + 1 - max_len and not visited[row][col]: 
                length = (DFS_up(row, col, 1, rooms[row][col]+1)
                          + DFS_down(row, col, 0, rooms[row][col]-1))
                if max_len < length: 
                    max_len = length
                    max_rooms.clear()
                    max_rooms.append(st)
                elif max_len == length: 
                    max_rooms.append(st)
    print(f'#{tc} {min(max_rooms)} {max_len}')