# from itertools import zip_longest
# T = int(input())
# for tc in range(1, T+1):
#     words = list(list(input()) for _ in range(5))
#     string = list(zip_longest(*words, fillvalue=''))
#     print(f'#{tc}', end=' ')
#     for s in string:
#         print("".join(s), end='')
#     print()

T = int(input())
for tc in range(1, T+1):
    bord = list(list('' for _ in range(15)) for _ in range(5))
    for i in range(5):
        string = input()
        for j in range(len(string)):
            bord[i][j] = string[j]
    print(f'#{tc}', end=' ')
    for i in range(15):
        for j in range(5):
            print(bord[j][i], end='')
    print()