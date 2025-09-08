from collections import deque
from copy import deepcopy as dcopy

def possible(brick_map, W, shots): 
    posscol = []
    trans = list(''.join(list(map(str, t))) for t in zip(*brick_map))
    for i in range(W): 
        brick = trans[i].lstrip('0')
        for j in range(shots): 
            if brick[j] != '1': 
                posscol.append((i, j)) # (col, 몇발 쏴야 하는지)
    return posscol

def break_brick(brick_map, col): 
    queue = deque([])
    dr, dc = [0, 1, 0], [1, 0, -1]
    for row in range(H): 
        if bricks[row][col] == 0: 
            continue
        elif bricks[row][col] == 1: 
            bricks[row][col] = 0
        else: 
            queue.append((row, col, bricks[row][col]-1))
            while queue: 
                brick = queue.popleft()
                for ofs in range(brick[2]): 
                    for r, c in zip(dr, dc): 
                        nrow, ncol = brick[0]+(r*ofs), brick[1]+(c*ofs)
                        if bricks[nrow][ncol] > 1: 
                            queue.append((nrow, ncol, bricks[nrow][ncol]-1))
                        bricks[nrow][ncol] = 0
            break
    


T = int(input())
for tc in range(1, T+1): 
    N, W, H = map(int, input().split())
    bricks = list(list(map(int, input().split())) for _ in range(H))
    queue = deque([])
    pos_col = possible(bricks, W)
    for pos in pos_col: 
        queue.append((pos[0], N-pos[1], dcopy(bricks)))
    while queue: 
        now = queue.popleft()
