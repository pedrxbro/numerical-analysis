# Função que calcula f(x)
def f(x):
    return x**3 - 6*x**2 + 11*x - 6.1

def devF(x):
    return 3*x**2 - 12*x + 11

# Testando a função
x = 3.0473
resultado = f(x)
derivative = devF(x)
print(f"O valor de f({x}) é {resultado:.4f}")
print(f"O valor de f'({x}) é {derivative:.4f}")
