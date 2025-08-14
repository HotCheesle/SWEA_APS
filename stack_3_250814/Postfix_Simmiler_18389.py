def get_prio_tok(op): 
    if op == '+' or op == '-': 
        return 1
    elif op == '*' or op == '/': 
        return 2

stack = []
top = -1

T = int(input())
for tc in range(1, T+1): 
    string = input().strip()
    print(f'#{tc} ', end='')
    for tok in string: 
        if tok in ['+', '-', '*', '/']: 
            prio = get_prio_tok(tok)
            if top == -1: 
                stack.append(tok)
                top += 1
            else: 
                while top != -1 and get_prio_tok(stack[top]) >= prio:
                    print(stack.pop(), end='')
                    top -= 1
                stack.append(tok)
                top += 1
        else: 
            print(tok, end='')
    for _ in range(len(stack)): 
        print(stack.pop(), end='')
        top -= 1
    print()
