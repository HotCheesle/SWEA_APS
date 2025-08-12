def pang(row, col, w, h): 
    tot = balloons[row][col]
    for ofs in range(-1, 2, 2): 
        if 0 <= (row + ofs) < h: 
            tot += balloons[row+ofs][col]
        if 0 <= (col + ofs) < w: 
            tot += balloons[row][col+ofs]
    return tot

T = int(input())
for tc in range(1, T+1): 
    height, width = map(int, input().split())
    balloons = list(list(map(int, input().split())) for _ in range(height))
    
    pang_list = []
    for row in range(height): 
        for col in range(width): 
            pang_list.append(pang(row, col, width, height))
    max_pang = 0
    for p in pang_list: 
        if max_pang < p: 
            max_pang = p
    
    print(f'#{tc} {max_pang}')