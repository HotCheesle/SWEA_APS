prio = {'+': 1, '*': 2}

for tc in range(1, 11): 
    stack = []
    postfix = []
    top = -1
    N = int(input())
    string = input()
    for tok in string: 
        if tok in ['+', '*']: 
            if top == -1: 
                stack.append(tok)
                top += 1
            else: 
                while top != -1 and prio[stack[top]] >= prio[tok]: 
                    postfix.append(stack.pop())
                    top -= 1
                stack.append(tok)
                top += 1
        else: 
            postfix.append(tok)
    if stack: 
        while top != -1: 
            postfix.append(stack.pop())
            top -= 1
    
    for tok in postfix: 
        if tok.isnumeric(): 
            stack.append(int(tok))
        elif tok == '+': 
            x2 = stack.pop()
            x1 = stack.pop()
            result = x1 + x2
            stack.append(result)
        else: 
            x2 = stack.pop()
            x1 = stack.pop()
            result = x1 * x2
            stack.append(result)
    print(f'#{tc} {stack.pop()}')