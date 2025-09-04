def brute_force(row, col, tot, N): # 재귀적으로 가장 작은 값을 반환함
    if row == N and col == N:      # 종료조건으로 현재 row와 col이 N에 도달했을 때 현재까지의 
        return tot                 # 총합을 return 한다.
    if row+1 > N:   # 만약 가장 아래쪽에 도달했으면 길이 오른쪽으로 가는것 하나밖에 없으므로 
        return brute_force(row, col+1, tot+board[row][col+1], N)
    elif col+1 > N: # 만약 가장 오른쪽에 도달했으면 길이 아래쪽으로 가는 것 하나밖에 없으므로 
        return brute_force(row+1, col, tot+board[row+1][col], N)
    else:           # 양쪽 다 갈 수 있다면 양쪽 다 재귀적으로 호출 후 반환값 중 작은것을 선택
        return min(brute_force(row, col+1, tot+board[row][col+1], N), 
                   brute_force(row+1, col, tot+board[row+1][col], N))

T = int(input())
for tc in range(1, T+1):
    N = int(input()) 
    board = list(list(map(int, input().split())) for _ in range(N)) # 입력 받기
    min_sum = brute_force(0, 0, board[0][0], N-1) # 초기값으로 row와 col은 (0, 0)이고, 총합은
    print(f'#{tc} {min_sum}')                 # (0, 0)의 값, N에 마지막 인덱스인 N-1을 넣어줌