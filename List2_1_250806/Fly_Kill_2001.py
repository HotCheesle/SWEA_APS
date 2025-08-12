T = int(input())

def kill_count(r, c):
    kill = 0
    for i in range(M):
        for j in range(M):
            kill += flys[r+i][c+j]
    return kill


for tc in range(1, T+1):
    N, M = map(int, input().split())

    flys = list(list(map(int, input().split())) for _ in range(N))
    max_kill = 0
    for row in range(N-M+1):
        for col in range(N-M+1):
            f_kill = kill_count(row, col)
            if max_kill < f_kill:
                max_kill = f_kill

    print(f'#{tc} {max_kill}')