"""
  Description: Given a matrix of NxN rotate the matrix by 90 degrees t
  times in place
  Author: Christian Consuelo
"""

def _rotate_matrix(matrix):
  for y, row in enumerate(matrix):
    for x, cell in enumerate(row[:len(row) - (len(row) - y)]):
      temp = matrix[y][x]
      matrix[y][x] = matrix[x][y]
      matrix[x][y] = temp

  for y, row in enumerate(matrix):
    for x, cell in enumerate(row[:len(row) / 2]):
      temp = matrix[y][x]
      matrix[y][x] = matrix[y][len(row) - 1 - x]
      matrix[y][len(row) - 1 - x] = temp

  return matrix

def rotate_matrix(matrix, times):
  times = times % 4

  for t in range(times):
    matrix = _rotate_matrix(matrix)

  return matrix

def print_matrix(matrix):
  for row in matrix:
    print(','.join([str(cell) for cell in row]))

matrix = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25]
]

print_matrix(rotate_matrix(matrix, 999))
