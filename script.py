class Person :
    def __init__(self, name='Joe', x=0, y=0) :
        self.name = name
        self.x = x
        self.y = y
    def move (self, x, y) :
        self.x = x
        self.y = y
    
    def get_location (self) :
        return [self.x, self.y]

class Grid :
    def __init__(self, height, width) :
        self.height = height
        self.width = width
        self.grid = [[' ' for g in range(width)] for i in range(height)]

        self.people = []

    def get_input (self) :
        allowable_responses = ['up', 'left', 'down', 'right']
        print('\nWhere do you want to move?\nUp, Down, Left, or Right')
        user_input = input().lower()
        incorrect_input = True
        while incorrect_input :
            if user_input in allowable_responses :
                incorrect_input = False
            else :
                print('Invalid input! Please enter up, down, left, or right')
                user_input = input('\nWhere do you want to move?\nUp, Down, Left, or Right').lower()
        else :
            return user_input

    def refresh_field (self) :
        self.grid = [[' ' for g in range(self.width)] for i in range(self.height)]

    def move_person (self, person) :
        move = self.get_input()
        x = person.get_location()[0]
        y = person.get_location()[1]
        max_x = self.width
        min_x = 0
        max_y = self.width
        min_y = 0
        if move == 'right' and person.x < max_x :
            x += 1
        elif move == 'left' and person.x > min_x :
            x -= 1
        elif move == 'up' and person.y < max_y :
            y += 1
        elif move == 'down' and person.y > min_y :
            y -= 1
        
        person.move(x, y)
        self.grid[-y][x] = 'P'

    def turn (self) :
        self.refresh_field()
        for person in self.people :
            self.move_person(person)
        for i in range(self.height) :
            line = ''
            for item in self.grid[i] :
                line += item
            line += '\n'
            print(line)
    
    def add_person (self, person) :
        self.people.append(person)







myhouse = Grid(22, 22)
kaleb = Person('Kaleb', 3, 3)
myhouse.add_person(kaleb)

while True :
    myhouse.turn()