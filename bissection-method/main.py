def calculateC(a, b):
    return (a + b)/2

def inputData():
    global n
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))

    n = int(input("Digite o número de termos: "))
    for i in range (n):
        quoficient.append(float(input(f"Digite o quoficiente do termo {i + 1}: ")))
        power.append(float(input(f"Digite o expoente do termo {i + 1}: ")))

    toler = float(input("Digite o erro percentual: "))
    iterMax = int(input("Digite o número máximo de iterações: "))

    return a,b, toler, iterMax

def calculateF(x):
    result = 0
    for i in range (n):
        result += quoficient[i] * (x ** power[i])
    return result

def bissectionMethod(a, b, toler, iterMax):
    iter = 0
    error = 100
    fA = calculateF(a)
    fB = calculateF(b)

    cOld = calculateC(a,b)

    if(fA * fB > 0):
        print("Não há raiz no intervalo")
        return None
    
    while(error > toler and iter < iterMax):
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

        if(iter > 0):
            error = abs((c - cOld) / c) * 100
        cOld = c

        iter += 1
        print(f"Iteração: {iter} - Raíz: {c:.4f} - Erro: {error:.4f}%")

    return c

# Dados de teste (Exercício 1)
# quoficient = [5, -5, 6, -2]
# power = [3,2,1,0]
# n = 4

# Dados de teste (Exercício 2)
quoficient = [-2, -1.5, 10, 2]
power = [6,4,1,0]
n = 4


#quoficient = []
#power = []
#n = 0

def Main():
    # Entrar com dados
    #a, b, toler, iterMax = inputData()

    
    # Dados de teste (Exercício 1)
    #a = 0
    #b = 1
    #toler = 10
    #iterMax = 10

    # Dados de teste (Exercício 2)
    a = -1
    b = 1
    toler = 5
    iterMax = 10

    raiz = bissectionMethod(a, b, toler, iterMax)
    print(f"Raíz: {raiz:.4f}")

if __name__ == "__main__":
    Main()