def hex_to_bin(hex): 
    if hex == 'A': 
        deci = 10
    elif hex == 'B': 
        deci = 11
    elif hex == 'C': 
        deci = 12
    elif hex == 'D': 
        deci = 13
    elif hex == 'E': 
        deci = 14
    elif hex == 'F': 
        deci = 15
    else: 
        deci = int(hex)
    bin = ''
    d = 3
    for _ in range(4): 
        bit = deci // 2**d
        bin += str(bit)
        deci -= 2**d * bit
        d -= 1
    return bin

T = int(input())
for tc in range(1, T+1): 
    _, hex_sequence = input().strip().split()
    bit_sequence = ''
    for hex in hex_sequence: 
        bit_sequence += hex_to_bin(hex)
    print(f'#{tc} {bit_sequence}')