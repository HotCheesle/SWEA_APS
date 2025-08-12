T = int(input())

def nearby_diff(row, col):
    sum_diff = 0
    for i in range(-1, 2, 2):
        if -1 < row + i < N:
            sum_diff += abs(mixed_list[row][col] - mixed_list[row+i][col])
        if -1 < col + i < N:
            sum_diff += abs(mixed_list[row][col] - mixed_list[row][col+i])
    return sum_diff

for tc in range(1, T+1):
    N = int(input())
    mixed_list = list(list(map(int, input().split())) for _ in range(N))
    tot_diff = 0
    for row in range(5):
        for col in range(5):
            tot_diff += nearby_diff(row, col)
    print(f'#{tc} {tot_diff}')
