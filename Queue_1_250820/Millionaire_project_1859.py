T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    price_list = list(map(int, input().split()))
    idx, tot = 0, 0
    while idx < N: 
        cur_max_price = max(price_list[idx:])
        while price_list[idx] != cur_max_price: 
            tot += (cur_max_price - price_list[idx])
            idx += 1
        idx += 1
    print(f'#{tc} {tot}')