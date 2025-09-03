def decoder(code): 
    if code == '0001101': 
        return 0
    elif code == '0011001': 
        return 1
    elif code == '0010011': 
        return 2
    elif code == '0111101': 
        return 3
    elif code == '0100011': 
        return 4
    elif code == '0110001': 
        return 5
    elif code == '0101111': 
        return 6
    elif code == '0111011': 
        return 7
    elif code == '0110111': 
        return 8
    elif code == '0001011': 
        return 9
    else: return None


T = int(input())
for tc in range(1, T+1): 
    N, M = map(int, input().split())
    signal = list(input() for _ in range(N))
    row, col = 0, 0
    for i in range(N): 
        for j in range(M-1, 50, -1): 
            if signal[i][j] == '1': 
                row, col = i, j
                break
        else:
            continue
        break
    col -= 55
    init_code = signal[row]
    even_sum, odd_sum = 0, 0
    for idx in range(8): 
        if idx % 2 == 0: 
            even_sum += decoder(init_code[col+(idx*7) : col+((idx+1)*7)])
        else: 
            odd_sum += decoder(init_code[col+(idx*7) : col+((idx+1)*7)])
    tot = even_sum*3 + odd_sum

    if tot % 10 == 0: 
        print(f'#{tc} {even_sum + odd_sum}')
    else: 
        print(f'#{tc} 0')