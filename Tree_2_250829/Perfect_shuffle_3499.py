import math

T = int(input())

for tc in range(1, T+1): 
    N = int(input())
    cards = list(input().split())
    half = cards[:math.ceil(len(cards)/2)].copy()
    f, b = 0, math.ceil(len(cards)/2)
    for i in range(N): 
        if i % 2 == 0: 
            cards[i] = half[f]
            f += 1
        else: 
            cards[i] = cards[b]
            b += 1
    print(f'#{tc}', end=' ')
    print(' '.join(cards))