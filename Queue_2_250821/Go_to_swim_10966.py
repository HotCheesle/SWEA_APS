from collections import deque

def not_BFS(queue,h, w, tot_dis, L_cnt): 
    while L_cnt != 0: 
        point = queue.popleft()
        for r, c in zip(dr, dc): 
            row = point[0] + r
            col = point[1] + c
            if 0 <= row < h and 0 <= col < w and lands[row][col] == 'L': 
                lands[row][col] = lands[point[0]][point[1]] + 1
                tot_dis += lands[row][col]
                L_cnt -= 1
                queue.append([row, col])
    return tot_dis

T = int(input())
for tc in range(1, T+1): 
    queue = deque([])
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    height, width = map(int, input().split())
    lands = list(list(input()) for _ in range(height))

    tot_dis, L_cnt = 0, 0
    for row in range(height): 
        for col in range(width): 
            if lands[row][col] == 'W': 
                for r, c in zip(dr, dc): 
                    if 0 <= row+r < height and 0 <= col+c < width and lands[row+r][col+c] == 'L': 
                        lands[row+r][col+c] = 1
                        tot_dis += 1
                        L_cnt -= 1
                        if [row+r, col+c] not in queue: 
                            queue.append([row+r, col+c])
            else: 
                L_cnt += 1
    tot_dis = not_BFS(queue, height, width, tot_dis, L_cnt)
    print(f'#{tc} {tot_dis}')