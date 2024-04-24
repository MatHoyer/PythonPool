class calculator:
  def __init__(self, object) -> None:
    self.object = object

  def __add__(self, object) -> None:
    for i in range(len(self.object)):
      self.object[i] += object
    print(self.object)

  def __mul__(self, object) -> None:
    for i in range(len(self.object)):
      self.object[i] *= object
    print(self.object)

  def __sub__(self, object) -> None:
    for i in range(len(self.object)):
      self.object[i] -= object
    print(self.object)

  def __truediv__(self, object) -> None:
    if object == 0:
      print("Division by zero is not allowed.")
      return
    for i in range(len(self.object)):
      self.object[i] /= object
    print(self.object)
