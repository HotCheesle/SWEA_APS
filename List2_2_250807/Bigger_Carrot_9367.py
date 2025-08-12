T = int(input())
for tc in range(1, T+1): 
    n = int(input())
    carrots = list(map(int, input().split()))
    max_straight = 1
    straight = 1
    for i in range(n-1): 
        if carrots[i+1] - carrots[i] > 0: 
            straight += 1
        else: 
            if max_straight < straight: 
                max_straight = straight
            straight = 1
    if max_straight < straight: 
        max_straight = straight
    print(f'#{tc} {max_straight}')
