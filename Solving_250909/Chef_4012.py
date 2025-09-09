def cook(N, food, cnt): 
    nfood = food.copy()
    if cnt >= N//2: 
        food_list.append(nfood)
        return None
    if not nfood: 
        st = 1
    else: 
        st = nfood[-1] + 1
    for fd in range(st, N+1): 
        if fd not in nfood: 
            nfood.append(fd)
            cook(N, nfood, cnt+1)
            nfood.pop()

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    matrix = list(list(map(int, input().split())) for _ in range(N))
    food_list = []
    cook(N, [], 0)
    min_dif = 10**9
    for food in food_list: 
        else_fd = [i for i in range(1, N+1) if i not in food]
        cook1, cook2 = 0, 0
        for fd1 in range(N//2): 
            for fd2 in range(fd1+1, N//2): 
                cook1 += matrix[food[fd1]-1][food[fd2]-1] + matrix[food[fd2]-1][food[fd1]-1]
                cook2 += matrix[else_fd[fd1]-1][else_fd[fd2]-1] + matrix[else_fd[fd2]-1][else_fd[fd1]-1]
        min_dif = min(min_dif, abs(cook1 - cook2))
    print(f'#{tc} {min_dif}')