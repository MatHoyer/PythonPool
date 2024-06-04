def give_bmi(height: list, weight: list) -> list[float]:
    '''
    Takes 2 lists of int or float that have the same length
    Return a list of float that contains the BMI of each person
    '''
    try:
        weightLen = len(weight)
        heightLen = len(height)
        if weightLen != heightLen or weightLen == 0 or heightLen == 0:
            raise ValueError("Bad weight or height.")
        bmi = []
        for i in range(weightLen):
            w = float(weight[i])
            h = float(height[i])
            bmi.append(w / (h ** 2))
        return bmi
    except ValueError as e:
        print(ValueError.__name__, ':', e)
        exit(1)


def apply_limit(bmi: list[float | int], limit: int) -> list[bool]:
    '''
    Takes a list of BMI and a BMI limit (max)
    Return a list of boolean that contains True if the BMI is over the limit
    '''
    boolTab = []
    try:
        bmiLen = len(bmi)
        if bmiLen == 0:
            raise ValueError("The length of the bmi is not good.")
        for i in range(bmiLen):
            b = float(bmi[i])
            boolTab.append(b > int(limit))
    except ValueError as e:
        print(ValueError.__name__, ':', e)
        exit(1)
    return boolTab
