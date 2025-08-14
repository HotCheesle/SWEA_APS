stack = []

T = int(input())
for tc in range(1, T+1): 
    stack.clear()
    code = input().split()
    for tok in code: 
        if tok.isdecimal(): 
            stack.append(int(tok))
        elif tok == '.': 
            result = stack.pop()
            if stack: 
                print(f'#{tc} error')
                break
        else: 
            try: 
                x2 = stack.pop()
                x1 = stack.pop()
            except: 
                print(f'#{tc} error')
                break
            if tok == '+': 
                result = x1 + x2
            elif tok == '-': 
                result = x1 - x2
            elif tok == '*': 
                result = x1 * x2
            elif tok == '/': 
                result = x1 // x2
            else: 
                print(f'#{tc} error')
                break
            stack.append(result)
    else: 
        print(f'#{tc} {result}')