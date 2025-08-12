def get_LPS(string): # LSP 리스트를 구하는 함수
    N = len(string)
    lps_list = [0 for _ in range(N+1)] # LSP 리스트
    for s in range(2, N+1): # 인덱스 벗어나는것 때문에 N+1
        sub = string[:s] # 각 서브스트링 별로 계산
        sub1 = sub[:s//2] # 접두사 부분
        sub2 = sub[s//2+(s%2):] # 접미사 부분
        left, cnt, max_cnt = 0, 0, 0 # 최대 길이만 측정
        for i in range(len(sub2)): 
            if sub1[left] == sub2[i]: # 같으면 길이 증가
                left += 1
                cnt += 1
            else: # 다르면 최대값 갱신
                if max_cnt < cnt: 
                    max_cnt = cnt
                cnt = 0
                left = 0
        if max_cnt < cnt: max_cnt = cnt
        lps_list[s] = max_cnt
    return lps_list # LPS반환

def KMP(find_str, str_in_here): # 실제 문자열을 순회하면서 검사하는 KMP함수
    lps = get_LPS(find_str) # LPS 리스트
    idx, find_idx = 0, 0
    while idx < len(str_in_here): # 문자열 순회
        if find_str[find_idx] == str_in_here[idx]: # 일치하면 찾는 문자열의 인덱스 증가
            find_idx += 1
        else: # 아니라면 lsp에서 값을 가져온다. 이때 문자열이 일치한적이 있다면 idx를 제자리에 있게 한다.
            if find_idx != 0: idx -= 1
            find_idx = lps[find_idx-1]
        idx += 1 # 항상 idx는 1씩 증가
        if find_idx >= len(find_str): # 찾는 문자열과 모두 일치한다면 True반환
            return True
    return False


T = int(input())
for tc in range(1, T+1): 
    str1 = input()
    str2 = input()
    if KMP(str1, str2): 
        print(f'#{tc} 1')
    else: 
        print(f'#{tc} 0')
