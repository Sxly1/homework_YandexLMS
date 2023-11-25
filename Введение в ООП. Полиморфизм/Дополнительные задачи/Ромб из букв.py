letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters1 = "ZYXWVUTSRQPONMLKJIHGFEDCBA"


class LettersRhombus:
    def __init__(self, lastletter, filler=" "):
        self.lastletter = lastletter
        self.filler = filler
        self.matrixlen = letters.index(self.lastletter) * 2 + 1
        self.lastindex = letters.index(self.lastletter)
        self.creatematrix()

    def creatematrix(self):
        a = [[self.filler] * self.matrixlen for i in range(self.matrixlen)]
        for y in range(self.matrixlen):
            for x in range(self.matrixlen):
                if x + y == self.lastindex or x - y == self.lastindex:
                    a[y][x] = letters[y]
                if y - x == self.lastindex:
                    a[y][x] = letters1[letters1.index(self.lastletter) + x]
                if y + x == self.lastindex + self.matrixlen - 1:
                    a[y][x] = letters1[letters1.index(self.lastletter) + (self.matrixlen - 1 - x)]

        self.matrix = a

    def rows(self):
        a = []
        for i in range(len(self.matrix)):
            append = ""
            for j in range(len(self.matrix[i])):
                append += self.matrix[i][j]
            a.append(append)
        return a

    def cols(self):
        a = []
        for i in range(len(self.matrix)):
            append = ""
            for j in range(len(self.matrix[i])):
                append += self.matrix[j][i]
            a.append(append)
        return a


lines = LettersRhombus("C")
print(*lines.cols(), sep="\n")