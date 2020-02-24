"""
  Description: If an element in an MxN matrix is 0,
  its entire row and column is set to 0
  Author: Christian Consuelo
"""

def rows_columns_to_0(matrix, y, x, M, N):
  for i in range(M):
    matrix[y][i] = 0
  
  for j in range(N):
    matrix[j][x] = 0

  return matrix

def zero_matrix(matrix, M, N):
  zeros = []

  for y, row in enumerate(matrix):
    for x, cell in enumerate(row):
      if matrix[y][x] == 0:
        zeros.append((y, x))

  for z in zeros:
      matrix = rows_columns_to_0(matrix, z[0], z[1], M, N)

  return matrix

def print_matrix(matrix):
  for row in matrix:
    print(','.join([str(cell) for cell in row]))

matrix = [
  [1, 1, 1, 0, 1],
  [1, 1, 1, 1, 1],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 1, 0, 1, 1],
]

# M = Number of columns
# N = Number of rows
print_matrix(zero_matrix(matrix, 5, 5))
