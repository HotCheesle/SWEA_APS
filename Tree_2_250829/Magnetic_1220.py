for tc in range(1, 11): 
    N = int(input())
    table = list(list(map(int, input().split())) for _ in range(N))
    cnt = 0
    for col in range(N): 
        stack = []
        for row in range(N): 
            if table[row][col] == 1: 
                stack.append(1)
            elif table[row][col] == 2: 
                if stack: 
                    cnt += 1
                    stack.clear()
    print(f'#{tc} {cnt}')