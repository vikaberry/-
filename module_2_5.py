def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
get_matrix(2, 2, 10)
get_matrix(3,2,5)
get_matrix(1,5,10)


