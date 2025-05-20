from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''King class that inherits from Baratheon and Lannister classes'''
    def __init__(self, name: str, is_alive: bool = True):
        '''Initialize the King member'''
        super().__init__(name, is_alive)

    def set_eyes(self, eyes: str):
        '''Set the eyes color of the King member'''
        self.eyes = eyes

    def get_eyes(self) -> str:
        '''Get the eyes color of the King member'''
        return self.eyes

    def set_hairs(self, hairs: str):
        '''Set the hairs color of the King member'''
        self.hairs = hairs

    def get_hairs(self) -> str:
        '''Get the hairs color of the King member'''
        return self.hairs
