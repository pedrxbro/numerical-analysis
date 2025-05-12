def backSubstituitionMethod(A, b):

    n  = len(A)
    x  = [0] * n

    for i in range(n -1 , -1, -1):
        soma = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - soma) / A[i][i]

    return x

if __name__ == "__main__":
    A = [
    [2, 1, -1],
    [0, 3, 1],
    [0, 0, 5]
    ]
    b = [8, 3, 5]

    solution = backSubstituitionMethod(A, b)
    print("Solução:", solution)
