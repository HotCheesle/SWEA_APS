def get_prio_tok(op): 
    if op == '+' or op == '-': 
        return 1
    elif op == '*' or op == '/': 
        return 2
    else: 
        return 3

def get_prio_stack(op): 
    if op == '+' or op == '-': 
        return 1
    elif op == '*' or op == '/': 
        return 2
    else: 
        return 0

stack = []
top = -1

T = int(input())
for tc in range(1, T+1): 
    string = input()
    print(f'#{tc} ', end='')
    for tok in string: 
        if tok in ['+', '-', '*', '/']: 
            prio = get_prio_tok(tok)
            if top == -1: 
                stack.append(tok)
                top += 1
            else: 
                while top != -1 and get_prio_stack(stack[top]) >= prio:
                    print(stack.pop(), end='')
                    top -= 1
                stack.append(tok)
                top += 1
        elif tok == '(': 
            stack.append(tok)
            top += 1
        elif tok == ')': 
            while stack[top] != '(': 
                print(stack.pop(), end='')
                top -= 1
            stack.pop()
            top -= 1
        else: 
            print(tok, end='')
    for _ in range(len(stack)): 
        print(stack.pop(), end='')
        top -= 1
    print()
