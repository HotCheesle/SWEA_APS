def get_repre(x, linked_list): 
    rep = linked_list.get(x)
    if rep is None: 
        for k, values in linked_list.items(): 
            if x in values: 
                rep = k
                break
    else: 
        rep = x
    return rep

T = int(input())
for tc in range(1, T+1): 
    N, M = map(int, input().split())
    elist = list(map(int, input().split()))
    linked_list = {i: {i} for i in range(1, N+1)}
    for idx in range(0, len(elist), 2): 
        key = get_repre(elist[idx], linked_list)
        val = get_repre(elist[idx+1], linked_list)
        if key == val: continue
        else: 
            linked_list[key].update(linked_list[val])
            linked_list.pop(val)
    print(f'#{tc} {len(linked_list)}')