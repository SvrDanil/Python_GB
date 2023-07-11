# Напишите функцию для транспонирования матрицы

def flip_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len((matrix[i]))):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(*matrix, sep="\n")
flip_matrix(matrix)
print()
print(*matrix, sep="\n")




