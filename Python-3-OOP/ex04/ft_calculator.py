class calculator:
  # decorator
  def dotproduct(V1: list[float], V2: list[float]) -> None:
    print('Dot product is: ', end='')
    print(sum([V1[i] * V2[i] for i in range(len(V1))]))

  # decorator
  def add_vec(V1: list[float], V2: list[float]) -> None:
    print('Add Vector is : ', end='')
    print([V1[i] + V2[i] for i in range(len(V1))])

  # decorator
  def sous_vec(V1: list[float], V2: list[float]) -> None:
    print('Sous Vector is : ', end='')
    print([V1[i] - V2[i] for i in range(len(V1))])
