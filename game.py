from threading import Lock

import random

class SingletonMeta(type):
    '''
    Возможность создания всего лишь одного экзепляра класса
    Каждый последующий раз при создании объекта из этого
    класса мы будем получать ссылку на предыдущий
    '''
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
    
class PotterCastle(metaclass=SingletonMeta):
    
    def __init__(self, size='7x7'):
        
        res = size.split('x')
        self.__width = int(res[0])
        self.__height = int(res[1])
        
        self.message = "Добро пожаловать"
        
        self.names = ["Подвал","Холл","Зал","Спальня","Кухня"]
        
        self.rooms_num = 5
        
        self.waysname = ["Вверх","Вниз","Влево","Вправо"]
        
        self.rooms = self.generate_castle()
        self.position = self.start_position()

    def move_position(self, way):
        if self.check_for_move(way):
            self.position = self.check_for_move(way)
            if self.rooms[self.position[0]][self.position[1]] == -1:
                
                kubik = random.randint(0, 3)
                if kubik == 1:
                    self.message = f"Поздравляем, вы вышли на улицу!"
                    self.room_name = "Выход"
                else:
                    self.rooms = self.generate_castle()
                    self.position = self.start_position()
                    self.message = f"Вы переместились в другую комнату"
            else:
                position = self.waysname[int(way)]
                self.message = f"Вы переместились {position}"
        else:
            self.message = "Вы не можете туда идти"

    def generate_castle(self) -> object:
        room_num = random.randint(0, self.rooms_num-1)
        self.room_name = self.names[room_num]
        
        rooms = [
            [random.randint(0, 7) for _ in range(self.__width)] for _ in range(self.__height)
        ]
        
        """формируем стены (обозначение - 0)"""
        for i in range(self.__width):
            rooms[0][i] = 0
            rooms[self.__height - 1][i] = 0
        for i in range(self.__height):
            rooms[i][0] = 0
            rooms[i][self.__width - 1] = 0
            
        """формируем выходы с каждой стороны (обозначение - -1)"""
        rooms[0][random.randint(1, self.__width - 2)] = -1
        rooms[self.__height - 1][random.randint(1, self.__width - 2)] = -1
        rooms[random.randint(1, self.__height - 2)][0] = -1
        rooms[random.randint(1, self.__height - 2)][self.__width - 1] = -1
        return rooms

    def get_name(self):
        return self.room_name

    def start_position(self):
        self.position = self.__height // 2, self.__width // 2
        while self.rooms[self.position[0]][self.position[1]] == 0:
            self.move_position(str(random.randint(0,len(self.waysname)-1)))
        return self.position

    def check_for_move(self, way):
        ways = {
            "0": (-1, 0),
            "1": (1, 0),
            "2": (0, -1),
            "3": (0, 1),
        }
        #print('way',way)
        step = ways[way]
        new_pos = (step[0] + self.position[0], step[1] + self.position[1])
        if self.__height < new_pos[0] or self.__width < new_pos[1]:
            return False
        elif self.rooms[new_pos[0]][new_pos[1]] == 0:
            return False
        else:
            return new_pos[0], new_pos[1]

