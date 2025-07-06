import math

def targetFunction(x):
    return (math.e**x**2)

def trapezoidalRule(func, a, b, n):
    h = (b - a) / n
    totalArea = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        x = a + i * h
        totalArea += func(x)
    return totalArea * h

def main():
    lowerLimit = 1.2
    upperLimit =  1.6
    subIntervals = 4  # número de trapézios

    result = trapezoidalRule(targetFunction, lowerLimit, upperLimit, subIntervals)
    print(f"Integral Aproximada: {result:.4f}")

if __name__ == "__main__":
    main()
