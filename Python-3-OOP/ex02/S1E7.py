from S1E9 import Character


class Baratheon(Character):
    '''Baratheon familly'''
    def __init__(self, name: str, is_alive: bool = True):
        '''Initialize the Baratheon familly member'''
        super().__init__(name, is_alive=is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self) -> str:
        '''Return the string representation of the Baratheon member'''
        name = self.__class__.__name__
        return f"Vector: ('{name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        '''Return the string representation of the Baratheon member'''
        name = self.__class__.__name__
        return f"Vector: ('{name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    '''Lannister familly'''
    def __init__(self, name: str, is_alive: bool = True):
        '''Initialize the Lannister familly member'''
        super().__init__(name, is_alive=is_alive)
        self.family_name = 'Lannister'

    def __str__(self) -> str:
        '''Return the string representation of the Lannister family member'''
        name = self.__class__.__name__
        return f"Vector: ('{name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        '''Return the string representation of the Lannister family member'''
        name = self.__class__.__name__
        return f"Vector: ('{name}', '{self.eyes}', '{self.hairs}')"

    @staticmethod
    def create_lannister(name: str, is_alive: bool = True):
        '''Create a Lannister member'''
        return Lannister(name, is_alive)
