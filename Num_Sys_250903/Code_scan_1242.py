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
    zeros = '0' * M
    hex_data_line = []
    for line in signal: 
        if line not in hex_data_line: 
            hex_data_line.append(line)
    hex_data_line.remove(zeros)
    
    bin_data_line = []
    for hex_line in hex_data_line: 
        bin_line = ''
        for hex in hex_line: 
            bin_line += hex_to_bin(hex)
        bin_line = bin_line.rstrip('0')
        possible_thickness = len(bin_line) // 56
        for thick in range(1, possible_thickness+1): 
            idx = len(bin_line)-1
            while idx > 50: 
                if bin_line[idx] == '1': 
                    if idx - (56*thick-1) < 0: break
                    bin_code = bin_line[idx-(56*thick-1) : idx+1]
                    if bin_code not in bin_data_line: 
                        bin_data_line.append(bin_code)
                    idx -= (56*thick-1)
                    continue
                idx -= 1
    
    tot_sum = 0
    for bin in bin_data_line: 
        interval = len(bin) // 56
        even_sum, odd_sum = 0, 0
        if interval != 1: 
            short_bin = ''
            for idx in range(0, len(bin), interval): 
                short_bin += bin[idx]
        else: 
            short_bin = bin
        for i in range(8): 
            if i % 2 == 0: 
                result = decoder(short_bin[i*7:(i+1)*7])
                if result is None: 
                    break
                else: 
                    even_sum += result
            else: 
                result = decoder(short_bin[i*7:(i+1)*7])
                if result is None: 
                    break
                else: 
                    odd_sum += result
        else: 
            if (even_sum + odd_sum) % 10 == 0: 
                tot_sum += (even_sum + odd_sum)

    print(f'#{tc} {tot_sum}')