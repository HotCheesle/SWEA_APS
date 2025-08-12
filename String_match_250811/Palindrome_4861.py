def find_palindrome(N, M, is_odd): 
    if is_odd: 
        for row in range(N): 
            for col in range(M//2, N-(M//2)): 
                for ofs in range(1, M//2+1): 
                    if palin[row][col+ofs] != palin[row][col-ofs]: 
                        break
                else: 
                    return row, col-M//2, True
        for col in range(N): 
            for row in range(M//2, N-(M//2)): 
                for ofs in range(M//2+1): 
                    if palin[row+ofs][col] != palin[row-ofs][col]: 
                        break
                else: 
                    return row-M//2, col, False
    else: 
        for row in range(N): 
            for col in range(M//2, N-(M//2)+1): 
                for ofs in range(M//2): 
                    if palin[row][col+ofs] != palin[row][col-ofs-1]: 
                        break
                else: 
                    return row, col-M//2, True
        for col in range(N): 
            for row in range(M//2, N-(M//2)+1): 
                for ofs in range(M//2): 
                    if palin[row+ofs][col] != palin[row-ofs-1][col]: 
                        break
                else: 
                    return row-M//2, col, False



T = int(input())
for tc in range(1, T+1): 
    N, M = map(int, input().split())
    palin = list(list(input()) for _ in range(N))
    row, col, is_row = find_palindrome(N, M, M%2 == 1)
    if is_row: 
        print(f'#{tc} {"".join(palin[row][col:col+M])}')
    else: 
        print(f'#{tc}', end=' ')
        for r in range(row, row+M): 
            print(palin[r][col], end='')
        print()