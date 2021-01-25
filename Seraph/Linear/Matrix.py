class MatrixDimension:
    def __init__(self, row, column):
        self.row = row
        self.column = column


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.dimension = MatrixDimension(len(matrix), len(matrix[0]))
    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            row_str = "\t".join(str(num) for num in row)
            matrix_str += "|" + row_str + "|\n"
        return matrix_str

    def __add__(self, other):
        new_matrix = [[0 for i in range(self.dimension.column)] for j in range(self.dimension.row)]
        for i in range(0,self.dimension.row):
            for j in range(0,self.dimension.column):
                new_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(new_matrix)
    def __mul__(self, other):
        new_matrix = [[0 for i in range(self.dimension.column)] for j in range(other.dimension.row)]
        for row in range(self.dimension.row):
            for column in range(self.dimension.column):
                new_element = 0
                for column_num in range(self.dimension.column):
                    new_element += self.matrix[row][column_num] * other.matrix[column_num][column]
                new_matrix[row][column] = new_element
        return Matrix(new_matrix)
    def transpose(self):
        new_matrix = [[0 for i in range(self.dimension.column)] for j in range(self.dimension.row)]
        for i in range(self.dimension.row):
            for j in range(self.dimension.column):
                new_matrix[j][i] = self.matrix[i][j]
        return Matrix(new_matrix)
