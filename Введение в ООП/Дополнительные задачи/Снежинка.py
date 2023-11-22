class SnowFlakes:
    def __init__(self, size):
        self.array = [["-"] * size for i in range(size)]
        self.size = size
        for x in range(size):
            for y in range(size):
                if x == y:
                    self.array[x][y] = "*"
                if y == size // 2:
                    self.array[x][y] = "*"
                if x == size // 2:
                    self.array[x][y] = "*"
                if x + y == size - 1:
                    self.array[x][y] = "*"

    def thaw(self, n):
        for i in range(n):
            for j in range(self.size):
                self.array[j][i] = "-"
                self.array[i][self.size - 1 - j] = "-"
                self.array[j][self.size - 1 - i] = "-"
                self.array[self.size - 1 - i][j] = "-"

    def thicken(self):
        for x in range(self.size):
            for y in range(self.size):
                if x == y:
                    self.array[x][y] = "*"
                if y == self.size // 2:
                    self.array[x][y] = "*"
                if x == self.size // 2:
                    self.array[x][y] = "*"
                if x + y == self.size - 1:
                    self.array[x][y] = "*"

        for x in range(self.size):
            for y in range(self.size):
                if self.array[x][y] == "*":
                    if x < self.size // 2 and y < self.size // 2:
                        if x == 0 and y == 0:
                            self.array[0][1] = "z"
                            self.array[1][0] = "z"
                        else:
                            self.array[x + 1][y] = "z"
                            self.array[x][y + 1] = "z"

                    if x < self.size // 2 and y > self.size // 2:
                        if x == self.size - 1 and y == 0:
                            self.array[0][self.size - 2] = "z"
                            self.array[1][self.size - 1] = "z"
                        else:
                            self.array[x][y - 1] = "z"
                            self.array[x + 1][y] = "z"

                    if x > self.size // 2 and y < self.size // 2:
                        if x == self.size - 1 and y == 0:
                            self.array[self.size - 1][1] = "z"
                            self.array[self.size - 2][0] = "z"
                        else:
                            self.array[x - 1][y] = "z"
                            self.array[x][y + 1] = "z"

                    if x > self.size // 2 and y > self.size // 2:
                        if x == self.size - 1 and y == self.size - 1:
                            self.array[self.size - 1][self.size - 2] = "z"
                            self.array[self.size - 2][self.size - 1] = "z"
                        else:
                            self.array[x - 1][y] = "z"
                            self.array[x][y - 1] = "z"

                    if y == self.size // 2:
                        self.array[x][y - 1] = "z"
                        self.array[x][y + 1] = "z"
                    if x == self.size // 2:
                        self.array[x - 1][y] = "z"
                        self.array[x + 1][y] = "z"

        for x in range(self.size):
            for y in range(self.size):
                if self.array[x][y] == "z":
                    self.array[x][y] = "*"

    def freeze(self, n):
        a = [["-"] * (self.size + n * 2) for i in range(self.size + n * 2)]
        for x in range(self.size + n * 2):
            for y in range(self.size + n * 2):
                if x == y:
                    a[x][y] = "*"
                if y == (self.size + n * 2) // 2:
                    a[x][y] = "*"
                if x == (self.size + n * 2) // 2:
                    a[x][y] = "*"
                if x + y == (self.size + n * 2) - 1:
                    a[x][y] = "*"
        self.array = a
        self.size += n * 2

    def show(self):
        for i in range(self.size):
            print(*self.array[i], sep="")