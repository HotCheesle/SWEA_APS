for tc in range(1, 11): 
    N = int(input())
    palin = list(list(input()) for _ in range(8))
    if N == 1: 
        print(f'#{tc} 64')
        continue

    cnt = 0
    for row in range(8): 
        for col in range(N//2, 9-(N//2)): 
            if N % 2 == 0: 
                for ofs in range(N//2): 
                    if palin[row][col+ofs] != palin[row][col-1-ofs]: 
                        break
                else: 
                    cnt += 1
            else: 
                if col == 8-(N//2): continue
                for ofs in range(1, N//2+1): 
                    if palin[row][col+ofs] != palin[row][col-ofs]: 
                        break
                else: 
                    cnt += 1
    
    for col in range(8): 
        for row in range(N//2, 9-(N//2)): 
            if N % 2 == 0: 
                for ofs in range(N//2): 
                    if palin[row+ofs][col] != palin[row-1-ofs][col]: 
                        break
                else: 
                    cnt += 1
            else: 
                if row == 8-(N//2): continue
                for ofs in range(1, N//2+1): 
                    if palin[row+ofs][col] != palin[row-ofs][col]: 
                        break
                else: 
                    cnt += 1
    print(f'#{tc} {cnt}')