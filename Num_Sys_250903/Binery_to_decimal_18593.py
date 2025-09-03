T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    bit_sequence = ''
    for _ in range(N): 
        bit_sequence += input().strip()
    deci = []
    num = 0     # 10진수
    decimal = 0 # 자리수
    for idx in range(7*10-1, -1, -1): 
        num += int(bit_sequence[idx]) * 2**decimal
        decimal += 1
        if decimal == 7: 
            decimal = 0
            deci.append(num)
            num = 0
    deci.reverse()
    print(f'#{tc} ', end='')
    print(' '.join(map(str, deci)))
