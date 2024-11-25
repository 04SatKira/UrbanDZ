def get_matrix (n, m, value):
    matrix = []
    row = n
    column = m
    for n in range (matrix.count(n)):
        matrix.append ([n]*n)
        break
    for m in range (column):
        matrix_new = matrix * m
        matrix_new = matrix.replace (value) 
        print (matrix_new)
get_matrix (2, 2, 10)
