def get_matrix (n, m, value):
    matrix = []
    matrix.append ([value] * n)
    matrix_new = matrix * m
    print (matrix_new)
get_matrix (0, 0, 0)