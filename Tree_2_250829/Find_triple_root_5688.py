# import math

# T = int(input())
# for tc in range(1, T+1): 
#     N = int(input())
#     result = math.cbrt(N)
#     float_part = result - int(result)
#     if float_part <= 10**(-8): 
#         print(f'#{tc} {int(result)}')
#     else: 
#         print(f'#{tc} -1')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    deci = len(str(N)) - 1
    min_d = deci // 3
    init = 10**min_d
    while init*init*init <= N: 
        if init*init*init == N:
            print(f'#{tc} {init}')
            break
        init += 1
    else: 
        print(f'#{tc} -1')