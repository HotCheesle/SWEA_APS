T = int(input())
for tc in range(1, T+1): 
    n, sums = map(int, input().split())

    sum_cnt = 0
    n_list = [i for i in range(1, 13)]
    for i in range(1<<12): 
        sub_set = []
        tot = 0
        for j in range(12): 
            if i & 1<<j: 
                sub_set.append(n_list[j])
        if len(sub_set) == n: 
            for s in sub_set: 
                tot += s
            if tot == sums: 
                sum_cnt += 1
    
    print(f'#{tc} {sum_cnt}')
