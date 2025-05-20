class calculator:
    '''Calculator class to perform vector operations'''
    def __init__(self, object) -> None:
        '''Initialize the calculator'''
        self.object = object

    def __add__(self, object) -> None:
        '''Add the object to the calculator'''
        for i in range(len(self.object)):
            self.object[i] += object
        print(self.object)

    def __mul__(self, object) -> None:
        '''Multiply the object to the calculator'''
        for i in range(len(self.object)):
            self.object[i] *= object
        print(self.object)

    def __sub__(self, object) -> None:
        '''Subtract the object from the calculator'''
        for i in range(len(self.object)):
            self.object[i] -= object
        print(self.object)

    def __truediv__(self, object) -> None:
        '''Divide the object from the calculator'''
        if object == 0:
            print("Division by zero is not allowed.")
            return
        for i in range(len(self.object)):
            self.object[i] /= object
        print(self.object)
