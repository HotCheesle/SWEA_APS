T = int(input())
for tc in range(1, T+1):
    N, length = map(int, input().split())
    puzzle = list(list(map(int, input().split())) for _ in range(N))

    fit_cnt = 0
    for row in range(N):
        v_len, h_len = 0, 0
        for col in range(N):
            if puzzle[row][col] == 1:
                h_len += 1
            else:
                if h_len == length:
                    fit_cnt += 1
                h_len = 0
            if puzzle[col][row] == 1:
                v_len += 1
            else:
                if v_len == length:
                    fit_cnt += 1
                v_len = 0
        if h_len == length:
            fit_cnt += 1
        if v_len == length:
            fit_cnt += 1

    print(f'#{tc} {fit_cnt}')
