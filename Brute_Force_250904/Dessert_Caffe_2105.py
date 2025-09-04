from collections import deque

def BFS(row, col): 
    queue = deque([(row, col, 0, 0, set())])
    # row, col, direction, distance, visited
    max_cnt = -1
    while queue: 
        cur = queue.popleft()
        if 0 > cur[0] or cur[0] >= N or 0 > cur[1] or cur[1] >= N: 
            continue
        elif cur[3] != len(cur[4]): 
            continue
        elif cur[3] != 0 and cur[0] == row and cur[1] == col: 
            max_cnt = max(max_cnt, cur[3])
        elif cur[2] == 3 and cur[0] > row: 
            continue
        else: 
            cur[4].add(area[cur[0]][cur[1]])
            visited = cur[4].copy()
            queue.append((cur[0] + delta[cur[2]][0], 
                          cur[1] + delta[cur[2]][1], 
                          cur[2], 
                          cur[3]+1, 
                          visited))
            if cur[3] != 0 and cur[2] < 3: 
                visited = cur[4].copy()
                queue.append((cur[0] + delta[cur[2]+1][0], 
                            cur[1] + delta[cur[2]+1][1], 
                            cur[2]+1, 
                            cur[3]+1, 
                            visited
                            ))
    return max_cnt


T = int(input())
delta = [(-1, 1), (-1, -1), (1, -1), (1, 1)] # 차례대로 우상, 좌상, 좌하, 우하
for tc in range(1, T+1): 
    N = int(input())
    area = list(list(map(int, input().split())) for _ in range(N))
    max_dessert = -1
    for r in range(2, N): 
        for c in range(1, N-1): 
            dessert = BFS(r, c)
            max_dessert = max(max_dessert, dessert)
    print(f'#{tc} {max_dessert}')