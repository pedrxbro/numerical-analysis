def gaussSeidelMethod(A, b, x0, kMax, tol):

    n = len(A)
    x = x0.copy()

    for k in range(kMax):
        xOld = x.copy()

        for i in range (n):
            soma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - soma) / A[i][i]

        error = max(abs(x[i] - xOld[i]) for i in range(n))
        if error < tol:
            break

    return x, k+1

if __name__ == "__main__":
    A = [
    [10, 2, 3],
    [1, 5, 1],
    [2, 3, 10]
    ]
    b = [7, -8, 6]

    x0 = [0, 0, 0]

    solution, iterations = gaussSeidelMethod(A, b, x0, 10, 0.01)
    print("Solução:", solution)
    print("Nº de iterações:", iterations)