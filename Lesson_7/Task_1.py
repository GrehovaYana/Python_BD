class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join("\t".join([f'{el:02}' for el in line]) for line in self.matrix)

    def __add__(self, other):
        try:
            n = [[int(self.matrix[line][el]) + int(other.matrix[line][el]) for el in range(len(self.matrix[line]))]
                 for line in range(len(self.matrix))]
            return Matrix(n)
        except IndexError:
            return f'Error in matrix size'


matrix_1 = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
matrix_2 = [[7, 8, 9], [9, 10, 11], [11, 12, 13]]

m_1 = Matrix(matrix_1)
m_2 = Matrix(matrix_2)

sum_matrix = m_1 + m_2
print(f" First matrix:\n{m_1} ")
print(f" Second matrix:\n{m_2}")
print(f" Sum of matrix:\n{sum_matrix}")
