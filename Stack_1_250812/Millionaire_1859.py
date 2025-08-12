T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    price = list(map(int, input().split()))
    tot, idx= 0, N-1
    while idx > -1: 
        flag_price = price[idx]
        while price[idx-1] <= flag_price and idx > 0: 
            tot += flag_price - price[idx]
            idx -= 1
        tot += flag_price - price[idx]
        idx -= 1
    print(f'#{tc} {tot}')