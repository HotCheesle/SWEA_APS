T = int(input())

for tc in range(1, T+1):
    N = int(input())
    inpt = input()
    seq_one, max_one = 0, 0
    for c in inpt:
        if c == '1':
            seq_one += 1
        else:
            if max_one < seq_one:
                max_one = seq_one
            seq_one = 0
    if max_one < seq_one:
        max_one = seq_one

    print(f'#{tc} {max_one}')
