T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    is_found = 0
    for i in range(len(str2) - len(str1) + 1):
        if str2[i] == str1[0]:
            for j in range(1, len(str1)):
                if str1[j] != str2[i+j]:
                    break
            else:
                is_found = 1
                break
    print(f'#{tc} {is_found}')
