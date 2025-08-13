def attach(length_left): 
    if length_left <= 10: 
        return 1
    return attach(length_left-10) + (2 * attach(length_left-20))

T = int(input())
for tc in range(1, T+1): 
    length = int(input())
    cnt = attach(length)
    print(f'#{tc} {cnt}')