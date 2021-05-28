from .human import Human

class Employee(Human):
    def __init__(self, position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position
