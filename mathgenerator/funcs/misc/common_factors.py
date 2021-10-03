from .__init__ import *


def commonFactorsFunc(maxVal=100):
    a = x = random.randint(1, maxVal)
    b = y = random.randint(1, maxVal)

    if (x < y):
        min = x
    else:
        min = y

    count = 0
    arr = []

    for i in range(1, min + 1):
        if (x % i == 0):
            if (y % i == 0):
                count = count + 1
                arr.append(i)

    problem = f"Common Factors of {a} and {b} = "
    solution = arr
    return problem, solution


common_factors = Generator("Common Factors", 40,
                           commonFactorsFunc,
                           ["maxVal=100"])
