class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def branch(self):
        if self.a > 0:
            return "up"
        else:
            return "down"

    def x_sect(self):
        D = self.b ** 2 - (4 * self.a * self.c)
        if D > 0:
            return 2
        if D == 0:
            return 1
        if D < 0:
            return 0

    def y_sect(self):
        return (0, self.c)

    def sections(self):
        D = self.b ** 2 - (4 * self.a * self.c)
        if D < 0:
            return None
        if D == 0:
            return ((-1 * self.b) / 2 * self.a, 0.0)
        else:
            x1 = (-1 * self.b + D ** 0.5) / (2 * self.a)
            x2 = (-1 * self.b - D ** 0.5) / (2 * self.a)
            if x1 < x2:
                return (x1, 0.0, x2, 0.0)
            else:
                return (x2, 0.0, x1, 0.0)

    def top(self):
        x = (-1 * self.b) / (2 * self.a)
        y = (4 * self.a * self.c - self.b ** 2) / (4 * self.a)
        return (x, y)