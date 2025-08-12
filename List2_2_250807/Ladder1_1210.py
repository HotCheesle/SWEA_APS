def up_ladders(start): 
    col = start
    for row in range(99, -1, -1): 
        direc = is_side(row, col)
        if direc == 1: 
            while col < 99 and ladders[row][col+1] == 1: 
                col += 1
        elif direc == -1: 
            while col > 0 and ladders[row][col-1] == 1: 
                col -= 1
    return col

def is_side(row, col): 
    if col+1 < 100 and ladders[row][col+1] == 1: 
        return 1
    if col-1 >= 0 and ladders[row][col-1] == 1: 
        return -1
    return 0

for tc in range(1, 11): 
    t = int(input()) # 사용안함
    ladders = list(list(map(int, input().split())) for _ in range(100))
    x_idx = 0
    for i in range(100): 
        if ladders[99][i] == 2: 
            x_idx = i
            break
    print(f'#{tc} {up_ladders(x_idx)}')