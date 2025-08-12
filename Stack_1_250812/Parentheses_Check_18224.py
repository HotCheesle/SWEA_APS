def s_push(par): 
    global top
    top += 1
    stack[top] = par

def s_pop(): 
    global top
    if top == -1: 
        return None
    data = stack[top]
    top -= 1
    return data

stack = [None for _ in range(1000)]
top = -1
T = int(input())
for tc in range(1, T+1): 
    string = input()
    for i in range(len(string)): 
        if string[i] in ['(', ')', '{', '}']: 
            if string[i] == '(': 
                s_push('(')
            elif string[i] == '{': 
                s_push('{')
            elif string[i] == ')': 
                if s_pop() != '(':
                    print(f'#{tc} 0')
                    break
            else: 
                if s_pop() != '{':
                    print(f'#{tc} 0')
                    break
    if top == -1: 
        print(f'#{tc} 1')
    else: 
        print(f'#{tc} 0')