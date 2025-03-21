quoficient = []
power = []
n = 0

def calculateC(a, b):
    return (a + b)/2

#test
def inputData():
    global n
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))

    n = int(input("Digite o número de termos: "))
    for i in range (n):
        quoficient.append(int(input(f"Digite o quoficiente do termo {i + 1}: ")))
        power.append(n - 1 - i)

    toler = int(input("Digite o erro percentual: "))
    iterMax = int(input("Digite o número máximo de iterações: "))

    return a,b, toler, iterMax

def calculateF(x):
    result = 0
    for i in range (n):
        result += quoficient[i] * (x ** power[i])
    return result

def bissectionMethod(a, b, toler, iterMax):
    iter = 0
    erro = 100
    fA = calculateF(a)
    fB = calculateF(b)

    if(fA * fB > 0):
        print("Não há raiz no intervalo")
        return None
    
    while(erro > toler and iter < iterMax):
        c = calculateC(a,b)
        fC = calculateF(c)

        if(fA * fC < 0): # Raíz está entre A e C
            b = c
            fB = fC
        elif (fC * fB < 0): # Raíz está entre B e C
            a = c 
            fA = fC
        else: # C =  0, portanto, foi encontrado.
            break

        erro = abs((b - a) / c) * 100
        iter += 1
        print(f"Iteração: {iter} - Raíz: {c} - Erro: {erro}")

    return c
def Main():
    a, b, toler, iterMax = inputData()
    raiz = bissectionMethod(a, b, toler, iterMax)
    print(f"Raíz: {raiz}")

if __name__ == "__main__":
    Main()
