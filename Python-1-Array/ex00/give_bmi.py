def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    weightLen = len(weight)
    heightLen = len(height)
    try:
        if weightLen != heightLen or weightLen == 0 or heightLen == 0:
            raise ValueError("The length of the weight or height are not good.")
        bmi = []
        for i in range(weightLen):
            w = float(weight[i])
            h = float(height[i])
            bmi.append(w / (h ** 2))
        return bmi
    except ValueError as e:
        print(ValueError.__name__, ':', e)
        exit(1)

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    boolTab = []
    bmiLen = len(bmi)
    try:
        if bmiLen == 0:
            raise ValueError("The length of the bmi is not good.")
        for i in range(bmiLen):
            b = float(bmi[i])
            boolTab.append(b > limit)
    except ValueError as e:
        print(ValueError.__name__, ':', e)
        exit(1)
    return boolTab