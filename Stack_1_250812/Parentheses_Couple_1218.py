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

def is_coupling(par): 
    for idx in range(4):
        if open_parenth[idx] == parenth[i]: 
            s_push(idx)
            return True
        if close_parenth[idx] == parenth[i]: 
            if s_pop() == idx: 
                return True
            else: 
                return False


open_parenth = ['(', '{', '[', '<']
close_parenth = [')', '}', ']', '>']
stack = [None for _ in range(1000)]
top = -1
for tc in range(1, 11): 
    N = int(input())
    parenth = input()
    for i in range(N): 
        if not is_coupling(parenth[i]): 
            print(f'#{tc} 0')
            break
    else: 
        if top == -1: 
            print(f'#{tc} 1')
        else: 
            print(f'#{tc} 0')