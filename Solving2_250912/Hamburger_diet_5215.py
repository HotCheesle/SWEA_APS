def get_max_taste(ingre, taste, cal, upper_cal): 
    if cal > upper_cal: 
        return
    if ingre: 
        st = ingre[-1]
    else: 
        st = 0
    for idx in range(st, N): 
        if idx not in ingre: 
            get_max_taste(ingre+[idx], taste+ingre_list[idx][0], 
                          cal+ingre_list[idx][1], upper_cal)
    taste_list.append(taste)


T = int(input())
for tc in range(1, T+1): 
    N, upper_cal = map(int, input().split())
    ingre_list = []
    for _ in range(N): 
        taste, cal = map(int, input().split())
        ingre_list.append((taste, cal))
    taste_list = []
    get_max_taste([], 0, 0, upper_cal)
    print(f'#{tc} {max(taste_list)}')