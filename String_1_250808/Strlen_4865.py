T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    char_list = [0 for _ in range(26)]
    ck_char = [0 for _ in range(26)]
    for c in str1:
        ck_char[ord(c)-65] += 1
    for c in str2:
        char_list[ord(c)-65] += 1
    max_cnt = 0
    for i in range(26):
        if ck_char[i] > 0 and max_cnt < char_list[i]:
            max_cnt = char_list[i]
    print(f'#{tc} {max_cnt}')