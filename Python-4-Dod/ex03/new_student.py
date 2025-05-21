import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''Generate a random 15-character string.'''
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    '''Class representing a student.'''
    name: str
    surname: str
    id: str = field(default_factory=generate_id, init=False)
    login: str = field(init=False)
    active: bool = True

    def __post_init__(self):
        '''Post-initialization processing.'''
        self.login = self.name[0] + self.surname
