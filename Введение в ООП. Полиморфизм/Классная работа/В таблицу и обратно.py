class LineToTable:
    def __init__(self, arr, y, x):
        self.arr = arr
        self.x = x
        self.y = y

    def resize(self):
        matrix = []
        arr = []
        c = 0
        for y in range(self.y):
            for x in range(self.x):
                arr.append(self.arr[c])
                c += 1
            matrix.append(arr)
            arr = []

        return matrix, self.y, self.x


class TableToLine:
    def __init__(self, matrix):
        self.matrix = matrix
        self.y = len(matrix)
        self.x = len(matrix[0])

    def resize(self):
        arr = []
        for y in range(self.y):
            for x in range(self.x):
                arr.append(self.matrix[y][x])

        return arr, self.y, self.x