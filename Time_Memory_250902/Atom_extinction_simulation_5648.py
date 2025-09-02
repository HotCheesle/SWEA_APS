# 15초라 시간 제한 걱정없이 탐색

class Plane(): 
    def __init__(self):
        self.atom_list = set()
        self.atom_cnt = 0
        self.tot_energy = 0

    def add_atom(self, x, y, dir, energy): 
        atom = Atom(x, y, dir, energy)
        self.atom_list.append(atom)
        self.atom_cnt += 1

    def move_half_sec(self): 
        remove_list = set()
        for atom in self.atom_list: 
            if atom.direction == 0: 
                atom.y += 1
            elif atom.direction == 1: 
                atom.y -= 1
            elif atom.direction == 2: 
                atom.x -= 1
            elif atom.direction == 3: 
                atom.x += 1
            if atom.x < -2000 or atom.x > 2000 or atom.y < -2000 or atom.y > 2000: 
                remove_list.add(atom)
                self.atom_cnt -= 1
        for rm in remove_list: 
            self.atom_list.remove(rm)

    def is_extinction(self): 
        position_list = set()
        collision_point = set()
        remove_list = set()
        for atom in self.atom_list: 
            if (atom.x, atom.y) in position_list: 
                collision_point.add((atom.x, atom.y))
            else:
                position_list.add((atom.x, atom.y))
        for idx in range(self.atom_cnt): 
            atom = self.atom_list[idx]
            if (atom.x, atom.y) in collision_point: 
                self.tot_energy += atom.energy
                self.atom_list.remove(atom)
                self.atom_cnt -= 1

class Atom(): 
    def __init__(self,x, y, direction, energy):
        self.x = x * 2
        self.y = y * 2
        self.direction = direction
        self.energy = energy

T = int(input())
for tc in range(1, T+1): 
    plane = Plane()
    N = int(input())
    for _ in range(N): 
        x, y, direction, energy = map(int, input().split())
        plane.add_atom(x, y, direction, energy)
    
    while plane.atom_cnt != 0: 
        plane.move_half_sec()
        plane.is_extinction()
    print(f'#{tc} {plane.tot_energy}')