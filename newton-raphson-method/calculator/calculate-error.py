def calculateError(x, xOld):
    return abs((x-xOld) /x) * 100

x = 3.0467
xOld = 3.0473
print(f"Erro: {calculateError(x, xOld):.4f}%")