def create_matrix(cols, rows):
  matrix = []
  for i in range(rows):
      row = []
      for i in range(cols):
          row.append(0)
      matrix.append(row)
      
  return matrix


rows = 3
cols = 4

My_matrix = create_matrix(cols,rows)

print(My_matrix)


