quoficient = []
power = []
n = 0

def inputData():
    global n
    x0 = int(input("Digite o valor de x0: "))
    n = int(input("Digite o número de termos: "))

    for i in range (n):
        quoficient.append(int(input(f"Digite o quoficiente do termo {i + 1}: ")))
        power.append(n - 1 - i)
        
    toler = float(input("Digite o erro percentual: "))
    iterMax = int(input("Digite o número máximo de iterações: "))
    return x0, toler, iterMax

def calculateF(x):
    result = 0
    for i in range (n):
        result += quoficient[i] * (x ** power[i])
    return result

def calculateDerivative(x):
    derivateQuoficient = []
    derivatePower = []

    for i in range (len(quoficient)):
        if(power[i] > 0):
            derivateQuoficient.append(quoficient[i] * power[i]) # Multiplica o quoficiente pela potência
            derivatePower.append(power[i] - 1) # Diminui a potência

    derivateValue = 0
    for i in range (len(derivateQuoficient)):
        derivateValue += derivateQuoficient[i] * (x ** derivatePower[i])
    return derivateQuoficient, derivatePower
    
def evaluatePolynomial(quoficient, power, x):
    return sum (quoficient * ( x ** power) for quoficient, power in zip(quoficient, power))

def newtonRaphsonMethod(x0, toler, iterMax):
    iter = 0
    erro = 100

    derivateQuoficient, derivatePower = calculateDerivative(x0)

    while(erro > toler and iter < iterMax):
        fx0 = calculateF(x0)
        fDerivateX0 = evaluatePolynomial(derivateQuoficient, derivatePower, x0)

        if fDerivateX0 == 0:
            print("Derivada igual a zero. Não é possível continuar") 
            return None
        
        xNext = x0 - (fx0 / fDerivateX0)
        erro = abs((xNext - x0) / xNext) * 100
        x0 = xNext
        iter += 1
        print(f"Iteração: {iter} - Raíz: {x0} - Erro: {erro}")
    return x0


def Main():
    x0, toler, iterMax = inputData()
    raiz = newtonRaphsonMethod(x0, toler, iterMax)
    print(f"Raíz: {raiz}")

    
if __name__ == "__main__":
    Main()
