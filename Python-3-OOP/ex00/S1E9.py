from abc import ABC, abstractmethod


class Character(ABC):
    '''Abstract class for characters'''
    @abstractmethod
    def __init__(self, name: str, is_alived: bool = True):
        self.first_name = name
        self.is_alive = is_alived

    def die(self):
        '''Kill the character'''
        self.is_alive = False
    

class Stark(Character):
    '''Stark familly inherits from character class'''
    def __init__(self, name: str, is_alived: bool = True):
        '''Initialize the Stark familly member'''
        super().__init__(name, is_alived)