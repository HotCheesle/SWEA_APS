T = int(input())
for tc in range(1, T+1): 
    p1 = [0 for _ in range(10)]
    p2 = p1.copy()
    cards = list(map(int, input().split()))
    end = 0
    for i in range(12): 
        if i % 2 == 0: 
            p1[cards[i]] += 1
            if i < 4: 
                continue 
            cnt = 0
            for card in p1: 
                if card: 
                    cnt += 1
                else: 
                    cnt = 0
                if cnt > 2 or card > 2: 
                    end = 1
        else: 
            p2[cards[i]] += 1
            if i < 4: 
                continue 
            cnt = 0
            for card in p2: 
                if card: 
                    cnt += 1
                else: 
                    cnt = 0
                if cnt > 2 or card > 2: 
                    end = 2
        if end: 
            break
    else: 
        print(f'#{tc} 0')
        continue
    if end == 1: 
        print(f'#{tc} 1')
    else: 
        print(f'#{tc} 2')