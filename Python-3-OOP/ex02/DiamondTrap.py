from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def __init__(self, name: str, is_alive: bool = True):
        Baratheon.__init__(self, name, is_alive)
        Lannister.__init__(self, name, is_alive)

    def set_eyes(self, eyes: str):
        self.eyes = eyes

    def get_eyes(self) -> str:
        return self.eyes
    
    def set_hairs(self, hairs: str):
        self.hairs = hairs

    def get_hairs(self) -> str:
        return self.hairs
