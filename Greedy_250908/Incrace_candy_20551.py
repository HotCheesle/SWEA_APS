T = int(input())
for tc in range(1, T+1): 
    boxes = list(map(int, input().split()))
    if boxes[2] < 3: 
        print(f'#{tc} -1')
        continue
    elif boxes[1] < 2: 
        print(f'#{tc} -1')
        continue
    tot = 0
    for idx in range(1, -1, -1): 
        if boxes[idx] >= boxes[idx+1]: 
            tot += boxes[idx] - boxes[idx+1] + 1
            boxes[idx] = boxes[idx+1] - 1
    print(f'#{tc} {tot}')