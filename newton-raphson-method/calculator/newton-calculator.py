def newton(x, fx, dfx):
    return x - (fx/dfx)

x0 = 3.0473
fx = 0.0014
dfx = 2.2905

result = newton(x0, fx, dfx)
print(f"O resultado de xi + 1 é: {result:.4f}")
