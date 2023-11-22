class Rainbow:
    def __init__(self, num=1):
        self.index = None
        if num % 2 == 0:
            self.colors = self.colors[::-1]

    colors = "red, orange, yellow, green, light blue, blue, violet".split(", ")

    def next_color(self, color):
        index = (self.colors.index(color) + 1) % len(self.colors)
        return self.colors[index]