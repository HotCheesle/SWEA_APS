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

stack = [None for _ in range(100000)]

T = int(input())
for tc in range(1, T+1): 
    top = -1
    tot, idx = 0, 0
    string = input()
    while idx < len(string):
        if string[idx] == '(': 
            if string[idx+1] == ')': 
                idx += 2
                tot += (top+1) # cur_pipe
            else: 
                s_push('(')
                tot += 1
                idx += 1
        else: 
            s_pop()
            idx += 1
    print(f'#{tc} {tot}')