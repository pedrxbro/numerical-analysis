def backSubstituitionMethod(A, b):

    n  = len(A)
    x  = [0] * n

    for i in range(n -1 , -1, -1):
        soma = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - soma) / A[i][i]

    return x

if __name__ == "__main__":
    A = [
    [3, 4, -5, 1],
    [0, 1, 3, -2],
    [0, 0, 4, -5],
    [0, 0, 0, 2]
    ]
    b = [-10, -1, 3, 2]

    solution = backSubstituitionMethod(A, b)
    print("Solução:", solution)
