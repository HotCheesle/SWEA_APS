def quick_sort(num_list, length, st, ed): 
    if length > 2: 
        piv_list = [st, st+length//2, ed]
        for i in range(2): 
            if num_list[piv_list[i]] > num_list[piv_list[i+1]]: 
                piv_list[i], piv_list[i+1] = piv_list[i+1], piv_list[i]
        if num_list[piv_list[0]] < num_list[piv_list[1]]: 
            piv_idx = piv_list[1]
            piv = num_list[piv_idx]
        else: 
            piv_idx = piv_list[0]
            piv = num_list[piv_idx]
        num_list[piv_idx], num_list[st] = num_list[st], num_list[piv_idx]
        s, e = st+1, ed
        while num_list[s] <= piv and s < ed: 
            s += 1
        while num_list[e] >= piv and e > st: 
            e -= 1
        while s < e: 
            num_list[s], num_list[e] = num_list[e], num_list[s]
            while num_list[s] <= piv and s < ed: 
                s += 1
            while num_list[e] >= piv and e > st: 
                e -= 1
        num_list[st], num_list[e] = num_list[e], num_list[st]
        quick_sort(num_list, e-st, st, e-1)
        quick_sort(num_list, ed-s+1, s, ed)
    elif length == 2: 
        if num_list[st] > num_list[ed]: 
            num_list[st], num_list[ed] = num_list[ed], num_list[st]
    return 

T = int(input())
for tc in range(1, T+1): 
    nlist = list(map(int, input().split()))
    quick_sort(nlist, len(nlist), 0, len(nlist)-1)
    print(f'#{tc} ', end='')
    print(*nlist)