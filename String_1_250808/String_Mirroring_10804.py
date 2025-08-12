T = int(input())
for tc in range(1, T+1):
    string = input()
    print(f'#{tc}', end=' ')
    for i in range(len(string)-1, -1, -1):
        if string[i] == 'p':
            print('q', end='')
        elif string[i] == 'q':
            print('p', end='')
        elif string[i] == 'b':
            print('d', end='')
        elif string[i] == 'd':
            print('b', end='')
    print()