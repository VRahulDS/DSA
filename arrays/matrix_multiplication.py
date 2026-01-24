def multiply(mat1, mat2):

    m1_rows = len(mat1)
    m1_cols = len(mat1[0])

    m2_rows = len(mat2)
    m2_cols = len(mat2[0])

    if m1_cols != m2_rows:
        return -1

    soln = []

    for m1r in range(m1_rows):
        row = []
        for m2c in range(m2_cols):
            ans = 0
            for m1c in range(m1_cols):
                ans += mat1[m1r][m1c] * mat2[m1c][m2c]
            row.append(ans)
        soln.append(row)
    
    return soln

print(multiply([[1,0,0],[0,1,0],[0,0,1]], [[1,2,3],[2,3,4],[3,4,5]]))


A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

print(multiply(A, B))

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

print(multiply(A, B))

A = [[1, 2, 3]]
B = [[4],
     [5],
     [6]]

print(multiply(A, B))

