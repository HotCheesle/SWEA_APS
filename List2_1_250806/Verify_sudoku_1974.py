T = int(input())
def verify_sudoku(sudo):
    for row in range(9):
        count = [0 for _ in range(10)]
        for col in range(9):
            count[sudo[row][col]] += 1
            count[sudo[col][row]] += 1
        for n in count[1:]:
            if n != 2:
                return 0
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if verify_block(sudo, row, col) == 0:
                return 0
    return 1

def verify_block(sudo, row, col):
    count = [0 for _ in range(10)]
    for r in range(3):
        for c in range(3):
            count[sudo[row+r][col+c]] += 1
    for n in count[1:]:
        if n != 1:
            return 0
    return 1

for tc in range(1, T+1):
    sudoku = list(list(map(int, input().split())) for _ in range(9))

    print(f'#{tc} {verify_sudoku(sudoku)}')