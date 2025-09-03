T = int(input())
for tc in range(1, T+1): 
    num = float(input())
    bit_sequence = ''
    for exp in range(1, 13): 
        bit = int(num // 2**(-exp))
        bit_sequence += str(bit)
        num -= 2**(-exp) * bit
        if num == 0.0: 
            break
    else: 
        print(f'#{tc} overflow')
        continue
    print(f'#{tc} {bit_sequence}')