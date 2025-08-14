def get_prio_tok(op): 
    if op == '+' or op == '-': 
        return 1
    elif op == '*' or op == '/': 
        return 2

stack = []
postfix = []

for tc in range(1, 11): 
    postfix.clear()
    stack.clear()
    top = -1
    _ = input()
    string = input().strip()
    for tok in string: 
        if tok in ['+', '-', '*', '/']: 
            prio = get_prio_tok(tok)
            if top == -1: 
                stack.append(tok)
                top += 1
            else: 
                while top != -1 and get_prio_tok(stack[top]) >= prio:
                    postfix.append(stack.pop())
                    top -= 1
                stack.append(tok)
                top += 1
        else: 
            postfix.append(int(tok))
    for _ in range(len(stack)): 
        postfix.append(stack.pop())
        top -= 1
    
    for tok in postfix:  
        if tok == '+': 
            x2 = stack.pop()
            x1 = stack.pop()
            result = x1 + x2
            stack.append(result)
        elif tok == '*': 
            x2 = stack.pop()
            x1 = stack.pop()
            result = x1 * x2
            stack.append(result)
        else: 
            stack.append(tok)
    print(f'#{tc} {stack.pop()}')
