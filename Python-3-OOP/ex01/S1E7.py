from S1E9 import Character


class Baratheon(Character):
    '''Baratheon familly'''
    def __init__(self, name: str, is_alive: bool = True):
        '''Initialize the Baratheon familly member'''
        super().__init__(name, eyes='brown', hairs='dark', is_alive=is_alive)

    def __str__(self) -> str:
        name = self.__class__.__name__
        return f"Vector: ('{name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        name = self.__class__.__name__
        return f"Vector: ('{name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    '''Lannister familly'''
    def __init__(self, name: str, is_alive: bool = True):
        '''Initialize the Lannister familly member'''
        super().__init__(name, eyes='blue', hairs='light', is_alive=is_alive)

    def __str__(self) -> str:
        name = self.__class__.__name__
        return f"Vector: ('{name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        name = self.__class__.__name__
        return f"Vector: ('{name}', '{self.eyes}', '{self.hairs}')"

    @staticmethod
    def create_lannister(name: str, is_alive: bool = True):
        '''Create a Lannister member'''
        return Lannister(name, is_alive)
