def init(i): 
    board[i][i] = 'W'
    board[i][i+1] = 'B'
    board[i+1][i] = 'B'
    board[i+1][i+1] = 'W'

dr, dc = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
stack = []

T = int(input())
for tc in range(1, T+1): 
    N, M = map(int, input().split())
    board = list(list('' for _ in range(N)) for _ in range(N))
    init(N//2-1)
    for m in range(M): 
        col, row, color = map(int, input().split())
        col -= 1
        row -= 1
        if color == 1: 
            color = 'B'
            opp = 'W'
        else: 
            color = 'W'
            opp = 'B'
        board[row][col] = color
        for r, c in zip(dr, dc): 
            if 0 <= row+r < N and 0 <= col+c < N and board[row+r][col+c] == opp: 
                ofs = 2
                stack.clear()
                stack.append((row+r, col+c))
                if (0 > row+(r*ofs) or row+(r*ofs) >= N 
                    or 0 > col+(c*ofs) or col+(c*ofs) >= N): 
                    continue
                while board[row+(r*ofs)][col+(c*ofs)] != color:
                    if (0 > row+(r*(ofs+1)) or row+(r*(ofs+1)) >= N 
                        or 0 > col+(c*(ofs+1)) or col+(c*(ofs+1)) >= N): 
                        break
                    elif board[row+(r*ofs)][col+(c*ofs)] == '': 
                        break
                    stack.append((row+(r*ofs), col+(c*ofs)))
                    ofs += 1
                else: 
                    for _ in range(len(stack)): 
                        c_row, c_col = stack.pop()
                        board[c_row][c_col] = color
    
    w_cnt, b_cnt = 0, 0
    for r in range(N): 
        for c in range(N): 
            if board[r][c] == 'W': 
                w_cnt += 1
            elif board[r][c] == 'B': 
                b_cnt += 1
    print(f'#{tc} {b_cnt} {w_cnt}')