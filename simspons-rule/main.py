import math

def targetFunction(x):
    return math.sqrt(x) + (1/x)

def simpsonOneThirdRule(func, a, b, n):
    if n % 2 != 0:
        raise ValueError("n precisa ser par.")
    h = (b - a) / n
    totalArea = func(a) + func(b)

    for i in range(1, n):
        x = a + i * h
        weight = 4 if i % 2 != 0 else 2
        totalArea += weight * func(x)
    return totalArea * h / 3

def main():
    upperLimit = 1.8
    lowerLimit = 1.4
    subIntervals = 4  # tem que ser PAR para Simpson 1/3

    result = simpsonOneThirdRule(targetFunction, lowerLimit, upperLimit, subIntervals)
    print(f"1/3 Simpson (n={subIntervals}): {result:.4f}")

if __name__ == "__main__":
    main()
