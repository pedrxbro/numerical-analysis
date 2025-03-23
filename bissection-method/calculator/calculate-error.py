def calculateError(c, cOld):
    return abs((c - cOld) / c) * 100


c = -0.1953
cOld =  -0.2031


print(f"Erro: {calculateError(c, cOld):.4f}")