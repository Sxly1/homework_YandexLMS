class RightMirror:
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_length = len(matrix)
        self.elem_length = len(matrix[0])

    def reflect(self):
        for y in range(self.matrix_length):
            for x in range(self.elem_length // 2):
                self.matrix[y][x], self.matrix[y][-1 * x - 1] = self.matrix[y][-1 * x - 1], self.matrix[y][x]
        return self.matrix


class BottomMirror:
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_length = len(matrix)
        self.elem_length = len(matrix[0])

    def reflect(self):
        for y in range(self.matrix_length):
            for x in range(self.elem_length // 2):
                self.matrix[y][x], self.matrix[y][-1 * x - 1] = self.matrix[y][-1 * x - 1], self.matrix[y][x]

        for y in range(self.matrix_length // 2):
            self.matrix[y], self.matrix[-1 * y - 1] = self.matrix[-1 * y - 1], self.matrix[y]
        return self.matrix