num_to_str = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for tc in range(1, T+1):
    count = [0 for _ in range(10)]
    _ = input()
    word_list = list(input().split())
    for word in word_list:
        for i in range(10):
            if word == num_to_str[i]:
                count[i] += 1
                break
    sort_list = []
    for i in range(10):
        sort_list.extend([num_to_str[i]] * count[i])
    print(f'#{tc}')
    print(' '.join(sort_list))