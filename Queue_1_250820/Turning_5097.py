class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None

def enqueue(head, tail, data): 
    new_node = Node(data)
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

def cycle(head, tail, M):
    for _ in range(M): 
        temp = head
        head = temp.next
        head.pre = None
        temp.next = None

        tail.next = temp
        temp.pre = tail
        tail = temp
    return head, tail

T = int(input())
for tc in range(1, T+1): 
    N, M = map(int, input().split())
    head, tail = None, None
    num_list = list(map(int, input().split()))
    for num in num_list: 
        head, tail = enqueue(head, tail, num)
    head, tail = cycle(head, tail, M)
    print(f'#{tc} {head.data}')