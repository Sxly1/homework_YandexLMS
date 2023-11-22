class JamesWebb:
    def __init__(self, data):
        self.data = data

    def brightest_star(self):
        max_y = None
        max_x = None
        max_star = 0
        for x in range(len(self.data)):
            for y in range(len(self.data[x])):
                if self.data[x][y] < 0 and abs(self.data[x][y]) > max_star:
                    max_star = abs(self.data[x][y])
                    max_y = y
                    max_x = x
        return (max_x, max_y)

    def brightest_galaxy(self):
        max_y = None
        max_x = None
        max_star = 0
        for x in range(len(self.data)):
            for y in range(len(self.data[x])):
                if self.data[x][y] > 0 and self.data[x][y] > max_star:
                    max_star = abs(self.data[x][y])
                    max_y = y
                    max_x = x
        return (max_x, max_y)

    def stars(self):
        quantity = 0
        for x in range(len(self.data)):
            for y in range(len(self.data[x])):
                if self.data[x][y] < 0:
                    quantity += 1
        return quantity

    def galaxies(self):
        quantity = 0
        for x in range(len(self.data)):
            for y in range(len(self.data[x])):
                if self.data[x][y] > 0:
                    quantity += 1
        return quantity

    def voids(self):
        quantity = 0
        for x in range(len(self.data)):
            for y in range(len(self.data[x])):
                if self.data[x][y] == 0:
                    quantity += 1
        return quantity