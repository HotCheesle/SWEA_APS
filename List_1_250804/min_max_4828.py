T = int(input())
for tc in range(1, T + 1):
    n  = int(input())
    min_n, max_n = 1000000, 0
    num_list = list(map(int, input().split()))
    for num in num_list:
        if min_n > num: min_n = num
        if max_n < num: max_n = num
    print(f'#{tc} {max_n - min_n}')