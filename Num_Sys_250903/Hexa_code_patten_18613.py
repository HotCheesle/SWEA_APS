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

def code_to_num(code): 
    if code == '001101': 
        return '0'
    elif code == '010011': 
        return '1'
    elif code == '111011': 
        return '2'
    elif code == '110001': 
        return '3'
    elif code == '100011': 
        return '4'
    elif code == '110111': 
        return '5'
    elif code == '001011': 
        return '6'
    elif code == '111101': 
        return '7'
    elif code == '011001': 
        return '8'
    elif code == '101111': 
        return '9'
    else: 
        return None

T = int(input())
for tc in range(1, T+1): 
    bit_sequence = ''
    hex_sequence = input().strip()
    for hex in hex_sequence: 
        bit_sequence += hex_to_bin(hex)
    bit_sequence = bit_sequence.rstrip('0')
    deci_list = []
    for idx in range(len(bit_sequence)-6, -1, -6): 
        deci_list.append(code_to_num(bit_sequence[idx:idx+6]))
    deci_list.reverse()
    print(f'#{tc} ', end='')
    print(' '.join(deci_list))