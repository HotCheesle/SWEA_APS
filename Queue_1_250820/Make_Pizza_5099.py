class Pizza: 
    def __init__(self, no, cheese):
        self.no = no
        self.cheese = cheese
        self.next = None
        self.pre = None

def enqueue(head, tail, no, cheese): 
    new_node = Pizza(no, cheese)
    if head is None or tail is None: 
        head = new_node
        tail = new_node
        return head, tail
    else: 
        tail.next = new_node
        new_node.pre = tail
        tail = new_node
        return head, tail

def dequeue(head, tail): 
    if head is None or tail is None: 
        return None
    else: 
        data = head.data
        head = head.next
        head.pre = None
        return head, tail, data

######################################

def cycle(head, tail, no):
    while head is not tail:
        temp = head
        head = temp.next
        head.pre = None
        temp.next = None
        temp.cheese //= 2
        if temp.cheese == 0: # 치즈가 0이면 새로 추가
            # print(f'pizza {temp.no} is done')
            if no == pizza_cnt+1: 
                # print('no queue pizza')
                continue
            head, tail = enqueue(head, tail, no, pizza_list[no-1])
            # print(f'pizza in no:{no}, cheese:{pizza_list[no-1]}')
            no += 1
        else: 
            tail.next = temp
            temp.pre = tail
            tail = temp
            # print(f'pizza {temp.no} is not yet cheese:{temp.cheese}')
    return head, tail

T = int(input())
for tc in range(1, T+1): 
    size, pizza_cnt = map(int, input().split())
    pizza_list = list(map(int, input().split()))
    no = 1
    head, tail = None, None
    for i in range(size): 
        head, tail = enqueue(head, tail, no, pizza_list[no-1])
        no += 1
    head, tail = cycle(head, tail, no)
    print(f'#{tc} {head.no}')