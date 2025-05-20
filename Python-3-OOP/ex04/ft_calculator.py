class calculator:
    '''Calculator class to perform vector operations'''
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''Calculate the dot product of two vectors'''
        print('Dot product is: ', end='')
        print(sum([V1[i] * V2[i] for i in range(len(V1))]))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''Add two vectors'''
        print('Add Vector is : ', end='')
        print([V1[i] + V2[i] for i in range(len(V1))])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''Subtract two vectors'''
        print('Sous Vector is : ', end='')
        print([V1[i] - V2[i] for i in range(len(V1))])
