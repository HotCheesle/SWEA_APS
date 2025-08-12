T = int(input())
for tc in range(1, T+1): 
    string = input().strip()
    N = len(string)
    if N % 2 == 0: 
        i = N//2
        for ofs in range(i): 
            if string[i+ofs] != string[i-ofs-1]: 
                print(f'#{tc} 0')
                break
        else: 
            print(f'#{tc} 1')
    else: 
        i = N//2
        for ofs in range(1, i+1): 
            if string[i+ofs] != string[i-ofs]: 
                print(f'#{tc} 0')
                break
        else: 
            print(f'#{tc} 1')