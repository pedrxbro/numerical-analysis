def gaussEliminationMethod(A, b):
    n = len(A)
    
    # Transforma a matriz em triangular superior
    for i in range(n):
        for j in range (i + 1, n):
            m = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] = A[j][k] - m * A[i][k]
            b[j] = b[j] - m * b[i]

    x = [0 for _ in range (n)]
    for i in range (n - 1, -1, -1):
        soma = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - soma) / A[i][i]

    return x

if __name__ == "__main__":
    A = [
    [10, 2, 3],
    [1, 5, 1],
    [2, 3, 10]
    ]
    b = [7, -8, 6]

    solution = gaussEliminationMethod(A, b)
    print("Solução:", solution)