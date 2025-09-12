class Petri_Dish: 
    def __init__(self, N, bact_list, K): 
        self.N = N
        self.K = K
        self.bacteria_list = bact_list

    def move_one_sec(self): 
        coord_list = set()
        coord_set = set()
        union_coord = dict()
        kill_coord = set()
        for Id in range(self.K): 
            if self.bacteria_list[Id] is None: continue
            coord = self.bacteria_list[Id].move()
            if coord in coord_set: 
                union_coord[coord] = []
            if coord[0] == 0 or coord[0] == N-1 or coord[1] == 0 or coord[1] == N-1: 
                kill_coord.add(coord)
            coord_list.add((Id, coord)) # (ID, (row, col))
            coord_set.add(coord)

        for Id, coord in coord_list: 
            if coord in union_coord.keys(): 
                union_coord[coord].append((Id, self.bacteria_list[Id].get_count(), self.bacteria_list[Id].get_dir()))
                self.bacteria_list[Id] = None
            elif coord in kill_coord: 
                self.bacteria_list[Id].kill_zone()
        
        for key, value in union_coord.items(): # key = coordinate, value = [(Id, cnt, dir), ]
            big_cnt, tot_cnt, union_id, union_dir = 0, 0, 0, 0
            for Id, cnt, dir in value: 
                if big_cnt < cnt: 
                    big_cnt = cnt
                    union_id = Id
                    union_dir = dir
                tot_cnt += cnt
            self.bacteria_list[union_id] = Bacteria(key[0], key[1], tot_cnt, union_dir)
    
    def show_all_cnt(self): 
        tot_cnt = 0
        for Id in range(self.K): 
            if self.bacteria_list[Id] is None: continue
            tot_cnt += self.bacteria_list[Id].get_count()
        return tot_cnt


class Bacteria: 
    dr, dc = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
    def __init__(self, row, col, count, direction):
        self.row = row
        self.col = col
        self.count = count
        self.direction = direction
    
    def move(self): 
        self.row += Bacteria.dr[self.direction]
        self.col += Bacteria.dc[self.direction]
        return (self.row, self.col)
    
    def kill_zone(self): 
        if self.direction == 1: 
            self.direction = 2
        elif self.direction == 2: 
            self.direction = 1
        elif self.direction == 3: 
            self.direction = 4
        else: 
            self.direction = 3
        self.count //= 2
    
    def get_count(self): 
        return self.count
    
    def get_dir(self): 
        return self.direction

T = int(input())
for tc in range(1, T+1): 
    N, M, K = map(int, input().split())
    bac_list = [None for _ in range(K)]
    for i in range(K): 
        bac_list[i] = Bacteria(*map(int, input().split()))
    plate = Petri_Dish(N, bac_list, K)
    for _ in range(M): 
        plate.move_one_sec()
    print(f'#{tc} {plate.show_all_cnt()}')