def pang_cnt(row, col, w, h):
    p = balloons[row][col]
    tot = p
    for ofs in range(1, p+1):
        if row+ofs < h:
            tot += balloons[row+ofs][col]
        if row-ofs >= 0:
            tot += balloons[row-ofs][col]
        if col+ofs < w:
            tot += balloons[row][col+ofs]
        if col-ofs >= 0:
            tot += balloons[row][col-ofs]
    return tot

T = int(input())
for tc in range(1, T+1):
    height, width = map(int, input().split())
    balloons = list(list(map(int, input().split())) for _ in range(height))
    max_pang = 0
    for row in range(height):
        for col in range(width):
            pang = pang_cnt(row, col, width, height)
            if max_pang < pang:
                max_pang = pang
    print(f'#{tc} {max_pang}')