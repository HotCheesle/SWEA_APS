pascal = list(list(0 for _ in range(10)) for _ in range(10))
pascal[0][0] = 1
for row in range(1, 10): 
    for col in range(row+1): 
        if col == 0 or col == row: 
            pascal[row][col] = 1
        else: 
            pascal[row][col] = pascal[row-1][col-1] + pascal[row-1][col]

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    print(f'#{tc}')
    for row in range(N): 
        for col in range(row+1): 
            print(pascal[row][col], end=' ')
        print()