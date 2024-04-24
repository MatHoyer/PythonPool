from abc import ABC, abstractmethod


class Character(ABC):
    '''Abstract class for characters'''
    @abstractmethod
    def __init__(self, name: str, eyes: str, hairs: str, is_alive: bool = True):
        '''Initialize the character'''
        self.first_name = name
        self.is_alive = is_alive
        self.family_name = self.__class__.__name__
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        '''Kill the character'''
        self.is_alive = False


class Stark(Character):
    '''Stark familly inherits from character class'''
    def __init__(self, name: str, is_alive: bool = True):
        '''Initialize the Stark familly member'''
        super().__init__(name, is_alive)