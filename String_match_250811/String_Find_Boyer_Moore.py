T = int(input())
for tc in range(1, T+1): 
    skip = [0 for _ in range(26)]
    str1 = input()
    str2 = input()
    N1 = len(str1)
    for i in range(len(str1)): 
        skip[ord(str1[i])-65] = i
    idx, find_idx = N1-1, 0
    while idx < len(str2): 
        if str1[find_idx] == str2[idx]: 
            find_idx += 1
            idx += 1
        else: 
            find_idx = 0
            if skip[ord(str2[idx])-65] != 0: 
                idx -= skip[ord(str2[idx])-65]
            else: 
                idx += N1
        if find_idx >= N1: 
            print(f'#{tc} 1')
            break
    else: 
        print(f'#{tc} 0')